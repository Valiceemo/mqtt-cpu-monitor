# MQTT CPU MONITOR

Simple python program

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
- Install required python modules listed in `requirements.txt`<br>
*psutil to grab boot time, cpu usage and temps, disk usage*<br>
*paho-mqtt to publish mqtt message(s) to your broker*<br>
*json to properly format json payload*
```bash
pip3 install -r requirements.txt
```

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

