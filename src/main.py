import json
import os
import paho.mqtt.client as mqtt
from lib.protocol import *
from lib.helper import get_product_name, get_operation_state_message, get_off_reason_message
from power_api import SixfabPower


device_id = os.environ.get('BALENA_DEVICE_UUID', default="default")

serial_port = os.getenv("SERIAL_PORT", default="/dev/ttyUSB0")
mqtt_broker = os.getenv("MQTT_BROKER", default="broker.hivemq.com")
mqtt_port = os.getenv("MQTT_PORT", default="1883")
mqtt_topic = os.getenv("MQTT_TOPIC", default=f"{device_id}/tronmon/uplink")

if __name__ == '__main__':

    ve = Vedirect(serial_port, 30)
    
    sixfab = SixfabPower()

    client = mqtt.Client()
    # TODO: Add try catch for MQTT connection
    client.connect(mqtt_broker, int(mqtt_port), 60)
    client.loop_start()

    def mqtt_send_callback(packet):

        payload = {
                # TODO: Improvee this
                'victron': {
                        'system': {
                                'serial': packet['SER#'],
                                'product_id': packet['PID'],
                                'product_name': get_product_name(packet['PID'])
                        },
                        'panel': {
                                'voltage': int(packet['VPV']) * .001,
                                'current': round(int(packet['PPV']) / int(packet['VPV']) * 1000, 2),
                                'power': int(packet['PPV'])
                        },
                        'battery': {
                                'voltage': int(packet['V']) * .001, 
                                'current': int(packet['I']) * .001,
                                'power': int(packet['VPV']) / 1000 * int(packet['I']) / 1000, 
                                'state': packet['CS'],
                                'state_message': get_operation_state_message(packet['CS']),
                                'off_reason': packet['OR'],
                                'off_reason_message': get_off_reason_message(packet['OR']),
                        }
                },
                'sixfab': {
                        'system': {
                                'voltage': sixfab.get_system_voltage(),
                                'current': sixfab.get_system_current(),
                                'power': sixfab.get_system_power(),
                                'temp': sixfab.get_system_temp(),
                                'fan_speed': sixfab.get_fan_speed(),
                                'fan_health': sixfab.get_fan_health(),
                                'fan_mode': sixfab.get_fan_mode()
                        },
                        'input': {
                                'voltage': sixfab.get_input_voltage(),
                                'current': sixfab.get_input_current(),
                                'temp': sixfab.get_input_temp(),
                                'power': sixfab.get_input_power()
                        },
                        'battery': {
                                'voltage': sixfab.get_battery_voltage(),
                                'current': sixfab.get_battery_current(),
                                'power': sixfab.get_battery_power(),
                                'temp': sixfab.get_battery_temp(),
                                'level': sixfab.get_battery_level(),
                                'health': sixfab.get_battery_health()
                        }
                }
        }

        client.publish(mqtt_topic, json.dumps(payload))

    ve.read_data_callback(mqtt_send_callback)