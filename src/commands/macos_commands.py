import psutil
from common_commands import *
import os

def shell_command(shell_command):
  return os.popen(shell_command).read().rstrip("\n\r")

## COMMANDS DEFINITIONS
# battery_percentage_command = "/usr/local/bin/istats | grep 'Current charge' | awk '{print $6}' | tr -dc '0-9\.'"
# ac_connected_command = "[[ \"$(system_profiler SPPowerDataType | grep Connected | awk '{print $2}')\" == \"Yes\" ]] && echo \"on\" || echo \"off\""
# CPU_percentage_command = "istats | grep 'CPU temp' | awk '{print $3}' | tr -dc '0-9\."
CPU_temperature_command = "/usr/local/bin/istats cpu | awk '{print $3}' | tr -dc '0-9\.'"
SSD_capacity_command = "df -h | grep /dev/disk1s1 | awk '{print $5}' | tr -dc '0-9\.'"
GPU_temperature_command = "/usr/local/bin/istats extra TG0D | awk '{print $6}' | tr -dc '0-9\.'"
battery_temperature_command = "/usr/local/bin/istats battery temp | awk '{print $3}' | tr -dc '0-9\.'"
battery_cycles_command = "/usr/local/bin/istats | grep 'Cycle count' | awk '{print $3}'"
ip_address = "ifconfig -a | grep 192.168. | awk '{print $2}'"

# shell publish (deprecared)
def mqtt_publish_sensor(sensor):
  mqtt_command = "mqtt pub -i asanchez -t %s -m %s -u %s -pw %s" % (sensor.getMqtt(), sensor.value, MQTT_USER, MQTT_PASS)
  # print(mqtt_command)
  sent_mqtt_command_result = shell_command(mqtt_command)
 
def macosCommands():
  return [
    ["battery_percentage", psutil.sensors_battery().percent],
    ["power_plugged", power_plugged()],
    ["cpu_percentage", psutil.cpu_percent(interval=1)],
    ["ram_percentage", psutil.virtual_memory().percent],
    ["cpu_temperature", shell_command(CPU_temperature_command)],
    ["gpu_temperature", shell_command(GPU_temperature_command)],
    ["battery_temperature", shell_command(battery_temperature_command)],
    ["battery_cycles", shell_command(battery_cycles_command)],
    ["ssd_capacity", shell_command(SSD_capacity_command)],
    ["ip_address", shell_command(ip_address)],
  ]