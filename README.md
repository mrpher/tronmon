![Victron](./docs/tronmon.png)

## What

Tronmon is a work-in-progress tool to monitor (and maybe one day control) Victron solar devices.  It utilizes a VE.Direct -> USB cable to capture metrics from any SmartSolar MPPT solar charger. When combined with a Raspberry Pi it permits sending those metrics wherever you like using the Paho MQTT library.

Currently it is configured to work with Victron's SmartSolar charge controllers, but could be easily adapted to any Victron device supporting the VE.Direct protocol.

## Why
I think you know why.

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
