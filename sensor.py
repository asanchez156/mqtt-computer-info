import platform
from environment import *

def prefix():
  if platform.system() == PLATFORM_MAC:
    return MQTT_MACOS_PREFIX
  else:
    return MQTT_WINDOWS_PREFIX

class Sensor:

  def __init__(self, name, value):
    self.name = name
    self.value = value

  def getMqtt(self):    
    return "%s%s/state" % (prefix(), self.name)
