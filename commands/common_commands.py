import psutil

def power_plugged(): 
  return "on" if psutil.sensors_battery().power_plugged else "off"
