import telnetlib
import time
import json

#our servers
payload = '[{"ip":"10.200.110.10", "port": "1101"},\
            {"ip":"10.200.110.10", "port": "1101"},\
            {"ip":"10.200.110.10", "port": "1101"},\
            {"ip":"10.200.110.10", "port": "1101"},\
            {"ip":"10.200.110.10", "port": "1101"},\
            {"ip":"10.200.110.10", "port": "1101"}\
          ]' 

def reload_telnet(ip_address, port, command):
    tn = telnetlib.Telnet(ip_address, port)
    tn.write(command.encode('ascii') + b"\n") # means pressing ENTER  
    time.sleep(1)

json_payload = json.loads(payload)

action = int(input("Command1 --> 1  Command2, bis_subs2 --> 2: "))
print(action)

for i in json_payload:
    reload_telnet(i["ip"], i["port"], "command") #follow out command
    reload_telnet(i["ip"], i["port"], "quit")    #then follow quit
    print(i["ip"] + ' ' + i["port"] + " command " + "Done!")

    if action == 2:
        reload_telnet(i["ip"], i["port"], "command")
        reload_telnet(i["ip"], i["port"], "quit")
        print(i["ip"] + ' ' + i["port"] + " command " + "Done!")


