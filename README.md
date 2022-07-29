![Victron](./docs/tronmon.png)

Tronmon is a work-in-progress tool to monitor (and maybe one day control) Victron solar devices.  It utilizes a VE.Direct -> USB cable to capture metrics from any SmartSolar MPPT solar charger. When combined with a Raspberry Pi it permits sending those metrics wherever you like using the Paho MQTT library.

Currently it is configured to work with Victron's SmartSolar charge controllers, but could be easily adapted to any Victron device supporting the VE.Direct protocol.

## Why
I think you know why.

## Requirements
You'll need a couple things to get started.
- Any [Victron](https://www.victronenergy.com/) device supporting VE.Direct, like the [SmartSolar MPPT 75/10](https://www.victronenergy.com/solar-charge-controllers/smartsolar-mppt-75-10-75-15-100-15-100-20#pd-nav-image)
- A [VE.Direct to USB](https://www.amazon.com/Victron-Energy-VE-Direct-USB-Cable/dp/B01LZ6WTLW) :warning:
- Any Raspberry Pi with a USB port
- A high quality [LiFePO4 battery](https://dakotalithium.com/product/dakota-lithium-12v-20ah-amp-hour-23ah-lifepo4-battery/)
- A [Sixfab PowerHAT](https://sixfab.com/product/raspberry-pi-power-management-ups-hat)



:warning: Yes, it's overpriced. Yes, you could make your own cable. No, it's not worth your time. Just buy the real thing.

## Configuration
Simple configuration can be done via environment variables.

|   Variable  |            Default            |                                                                Description                                                               |
|:-----------:|:-----------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|
| `SERIAL_PORT` | /dev/ttyUSB0                  | The serial port that corresponds to the VE.Direct connection                                                                             |
| `MQTT_BROKER` | broker.hivemq.com             | The MQTT broker URL                                                                                                                      |
| `MQTT_PORT`   | 1883                          | The MQTT broker port                                                                                                                     |
| `MQTT_TOPIC`  | { device_id } /tronmon/uplink | The default topic (ie. 1234567/tronmon/uplink). If BALENA_DEVICE_ID is not found, will default to "default" (ie. default/tronmon/uplink) |

## Credits
Tronmon is based largely on the incredible work from [karioja/vedirect](https://github.com/karioja/vedirect).

The core of which has been translated into the [lib/protocol.py](src/lib/protocol.py) library here.
