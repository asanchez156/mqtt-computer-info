# RUN on mac init: https://stackoverflow.com/questions/6442364/running-script-upon-login-mac

import time
import platform
from environment import *
from sensor import Sensor
from commands import Commands
import paho.mqtt.client as mqtt # https://pypi.org/project/paho-mqtt/

client = mqtt.Client("asanchez", True)
client.username_pw_set(MQTT_USER, MQTT_PASS)

sensor_list = []

def conection(status):
  connection = 'on' if status else 'off'
  return Sensor('mqtt_connection', connection)

def redefine_disconnect_mqtt_sensor_list():
  global sensor_list
  sensor_list = [connection(False)]

def redefine_sensor_list():
  global sensor_list
  sensor_list = [conection(True)] # connection status

  for command in Commands().list:
    sensor_list.append(Sensor(command[0], (command[1])))

def publish_sensor_list():
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

def daemon():
  print("Starting sensor tracking")
  while True:
    try:
      redefine_sensor_list()
      publish_sensor_list()
    # except KeyboardInterrupt:
    #   redefine_disconnect_mqtt_sensor_list()
    #   publish_sensor_list()
    #   print("press control-c again to quit")
    except Exception, e:
      print("Error!")
      print(e)
    # Sleep
    time.sleep(60)

daemon()
