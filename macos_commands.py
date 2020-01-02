## COMMANDS DEFINITIONS
battery_percentage_command = "istats | grep 'Current charge' | awk '{print $6}' | tr -dc '0-9\.'"
ac_connected_command = "[[ \"$(system_profiler SPPowerDataType | grep Connected | awk '{print $2}')\" == \"Yes\" ]] && echo \"on\" || echo \"off\""
# cpu percentage
# CPU_percentage_command = "istats | grep 'CPU temp' | awk '{print $3}' | tr -dc '0-9\."
# cpu temperature
CPU_temperature_command = "istats | grep 'CPU temp' | awk '{print $3}' | tr -dc '0-9\.'"
battery_temperature_command = "istats | grep 'Battery temp' | awk '{print $3}' | tr -dc '0-9\.'"
battery_cycles_command = "istats | grep 'Cycle count' | awk '{print $3}'"
# ram memory percentage
# ssd memory percentage
