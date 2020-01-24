# RUN on mac init: https://stackoverflow.com/questions/6442364/running-script-upon-login-mac

import time
from environment import *
from macos_commands import *
from sensor import Sensor
import paho.mqtt.client as mqtt # https://pypi.org/project/paho-mqtt/

client = mqtt.Client("asanchez", True)
client.username_pw_set(MQTT_USER, MQTT_PASS)

sensor_list = []

def redefine_sensor_list():
  global sensor_list
  sensor_list = []
  sensor_list.append(Sensor("battery_percentage", battery_percentage_command))
  sensor_list.append(Sensor("ac_connected", ac_connected_command))
  sensor_list.append(Sensor("cpu_temperature", CPU_temperature_command))
  sensor_list.append(Sensor("gpu_temperature", GPU_temperature_command))
  sensor_list.append(Sensor("battery_temperature", battery_temperature_command))
  sensor_list.append(Sensor("battery_cycles", battery_cycles_command))
  sensor_list.append(Sensor("ssd_capacity", SSD_capacity_command))

def iterate_this():
  redefine_sensor_list()
  for sensor in sensor_list:
    print("Sensor: %s. Value %s" % (sensor.name, sensor.value))

  # Connect to the broker
  print("Connecting..")
  client.connect(MQTT_HOST, MQTT_PORT, 60)

  print("Conected! Publishing...")
  for sensor in sensor_list:
    # publish sensor
    print(sensor.getMqtt(), sensor.value)
    client.publish(sensor.getMqtt(), sensor.value)

  # Disconnect
  print("Published! Disconnecting...")
  client.disconnect()

print("Starting sensor tracking")
while True:
  try:
    iterate_this()
  except:
    print("Error!")
  # Sleep
  time.sleep(60)
