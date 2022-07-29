#!/bin/bash
set -e

echo "Starting TronMon..."

# if [[ -z "${DEPLOY_ENV}" ]]

if [[ -z "${BALENA_DEVICE_UUID}" ]]; then
    echo "BALENA_DEVICE_UUID variable not found. Using 'default'."
else
    echo "BALENA_DEVICE_UUID: $BALENA_DEVICE_UUID"
fi

if [[ -z "${MQTT_BROKER}" ]]; then
    echo "MQTT_BROKER variable not found. Using 'localhost'."
else
    echo "MQTT_BROKER: $MQTT_BROKER"
fi

if [[ -z "${MQTT_TOPIC}" ]]; then
    echo "MQTT_TOPIC variable not found. Using '$BALENA_DEVICE_UUID/tronmon/uplink'."
else
    echo "MQTT_TOPIC: $MQTT_TOPIC"
fi

if [[ -z "${MQTT_PORT}" ]]; then
    echo "MQTT_PORT variable not found. Using '1883'."
else
    echo "MQTT_PORT: $MQTT_PORT"
fi

if [[ -z "${SERIAL_PORT}" ]]; then
    echo "SERIAL_PORT variable not found. Using '/dev/ttyUSB0'."
else 
    echo "SERIAL_PORT variable found. Using '$SERIAL_PORT'."
fi


# echo "127.0.0.1 $HOSTNAME" >> /etc/hosts

python main.py