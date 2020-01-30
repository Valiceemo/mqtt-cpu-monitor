# MQTT CPU MONITOR

Simple python program that will publish MQTT messages containing information about the system.  
Currently reported information  
* Boot time  
* CPU temperature  
* CPU usage as a percentage  
* Disk usage  

MQTT message is puiblished in json format to allow for easier processing by your broker.  
*Example message*
```json
{ timestamp: 16:10, boottime: 05/01/20 12:00, cpuusage: 5, cputemp: 45, disktotal: 8G }
```

Further details to follow

## SETUP

- Clone or download the repo to your machine, and move into the created directory
```
cd mqtt-cpu-monitor
```
- Set file permissions
```bash
sudo chmod +x cpu-monitor.py
sudo chmod 644 cpu-monitor.service
```
- Edit `cpu-monitor.py` to specify your mqtt broker and desire topic

- Copy / move systemd unit file 
poop
```bash
sudo mv cpu-monitor.service /etc/systemd/system/cpu-monitor.service
```
- Install required python modules listed in `requirements.txt`  
*psutil to grab boot time, cpu usage and temps, disk usage*  
*paho-mqtt to publish mqtt message(s) to your broker*  
*json to properly format json payload*  
```bash
pip3 install -r requirements.txt
```

## CONFIGURE

Edit the `cpu-monitor.py` file to your specific needs, and systems

- Enter your broker details
```bash
    broker="my-broker-ip"
    port="1883"
```
- Enter the mqtt topic name
```bash
topic = "my-topic/cpu"
```
- The reporting, i.e. publishing frequency can be set by modifying the `time.sleep` call  
By default it is set to 10 seconds


## START THE SERVICE

- Relaod the `systemd` process
```bash
sudo systemctl daemon-reload
```
- Start the service
```bash
sudo systemctl start cpu-monitor.service
```
- Enable the service to run at boot
```bash
sudo systemctl enable cpu-monitor.service
```

