# mqtt-computer-info

## Aim

This project is being done with the purpose of sending over mqtt my mac book status data.

> This data is being read from Home assistant sensor.

## Sent data

| Field  |  Value |
|---|---|
battery_percentage | int 
power_plugged | boolean 
cpu_percentage | int 
ram_percentage | int 
cpu_temperature | int 
gpu_temperature | int 
battery_temperature | int 
battery_cycles | int 
ssd_capacity | int 
ip_address | string 


## Home asistant examples
```yml
sensor:
 - platform: mqtt
   state_topic: "MY_NAME/macos/cpu_percentage/state"
   name: "Macbook CPU Usage"
   unit_of_measurement: "%"
   
 - platform: mqtt
   state_topic: "MY_NAME/macos/cpu_temperature/state"
   name: "Macbook CPU Temperature"
   unit_of_measurement: "ºC"
```
