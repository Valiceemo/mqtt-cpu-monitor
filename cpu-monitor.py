
#!/usr/bin/python3

# import modules
import os, psutil, sys
import paho.mqtt.client as mqtt
import time, datetime
import json

#
# idea: add means of checking if modules are available
#

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK, code", rc)
    else:
        print("Bad connection Returned code=",rc)
        client.bad_connection_flag=True

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


while true:
    mqtt.Client.connected_flag=False #create flag in class
    mqtt.Client.bad_connection_flag=False
    broker="192.168.0.45"
    port="1883"

    client = mqtt.Client("python1")

    client.on_connect=on_connect  #bind call back function

    client.loop_start()

    print("Connecting to broker",broker)

    try:
        client.connect(broker) #connect to broker
    except:
        print("connection failed")
        print(client.connected_flag)
        exit(1)

    while not client.connected_flag and not client.bad_connection_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    if client.bad_connection_flag:
        print(bad_connection_flag)
        client.loop_stop()    #Stop loop
        sys.exit()

###

    boottime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d/%m/%y %H:%M")
    currenttime = time.strftime("%Y-%m-%d %H:%M:%S")
    cputemp=int(float(getCPUtemperature()))
    cpupercent = psutil.cpu_percent(interval=1)
    disktotal = bytes2human( psutil.disk_usage('/').total )

    print("CPU Temp:",cputemp)
    print("CPU Usage",cpupercent,"%")
    print("Disk used",disktotal)

    topic = "pihole-monitor/cpu"
    payload = { 'timestamp': currenttime, 'boottime': boottime, 'cpuusage': cpupercent, 'cputemp': cputemp, 'disktotal': disktotal }

    print(payload)
    payload_json = json.dumps(payload)
    print(payload_json)
    client.publish(topic, payload_json)

    time.sleep(5)

