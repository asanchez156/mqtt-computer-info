import psutil
from common_commands import *

# ## COMMANDS DEFINITIONS
# # CPU_percentage_command = "istats | grep 'CPU temp' | awk '{print $3}' | tr -dc '0-9\."
# CPU_temperature_command = "/usr/local/bin/istats cpu | awk '{print $3}' | tr -dc '0-9\.'"
# SSD_capacity_command = "df -h | grep /dev/disk1s1 | awk '{print $5}' | tr -dc '0-9\.'"
# RAM_memory_command = ""
# GPU_temperature_command = "/usr/local/bin/istats extra TG0D | awk '{print $6}' | tr -dc '0-9\.'"
# battery_temperature_command = "/usr/local/bin/istats battery temp | awk '{print $3}' | tr -dc '0-9\.'"
# battery_cycles_command = "/usr/local/bin/istats | grep 'Cycle count' | awk '{print $3}'"

def windowsCommands():
  return [
    ["battery_percentage", psutil.sensors_battery().percent],
    ["power_plugged", power_plugged()],
    ["cpu_percentage", psutil.cpu_percent(interval=1)],
    ["ram_percentage", psutil.virtual_memory().percent],
    # ["ip_address", ip_address()]
  #   ["cpu_temperature", CPU_temperature_command],
  #   ["gpu_temperature", GPU_temperature_command],
  #   ["battery_temperature", battery_temperature_command],
  #   ["battery_cycles", battery_cycles_command],
  #   ["ssd_capacity", SSD_capacity_command],
  ]