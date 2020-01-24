import os
from environment import *

class Sensor:

  def __init__(self, name, shell_command):
    self.name = name
    self.shell_command = shell_command
    self.getShellCommandResult()

  def getMqtt(self):
    return "%s%s/state" % (MQTT_PREFIX, self.name)

  def getShellCommandResult(self):
    self.value = shell_command(self.shell_command)


def shell_command(shell_command):
  return os.popen(shell_command).read().rstrip("\n\r")

# shell publish
def mqtt_publish_sensor(sensor):
  mqtt_command = "mqtt pub -i asanchez -t %s -m %s -u %s -pw %s" % (sensor.getMqtt(), sensor.value, MQTT_USER, MQTT_PASS)
  # print(mqtt_command)
  sent_mqtt_command_result = shell_command(mqtt_command)