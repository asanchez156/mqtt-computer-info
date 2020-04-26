import psutil
import netifaces

def power_plugged(): 
  return "on" if psutil.sensors_battery().power_plugged else "off"


# NOT WORKING RETURNING u'IP_ADDRESS'
def ip_address(): 
  for iface in netifaces.interfaces():
    if iface == 'lo' or iface.startswith('vbox'):
      continue
    iface_details = netifaces.ifaddresses(iface)
    if iface_details.has_key(netifaces.AF_INET):
      # print iface_details[netifaces.AF_INET][0]['addr']
      if iface_details[netifaces.AF_INET][0]['addr'] != (u'127.0.0.1'):
        return iface_details[netifaces.AF_INET][0]['addr']

