# -*- coding: iso-8859-1 -*-
import subprocess, sys
from datetime import datetime
from telegramMsg import sendMessageToGroup
import socket
hostname = socket.gethostname()

p = subprocess.Popen(["powershell.exe", 
              "./madmax.ps1"], 
              stdout=sys.stdout)
p.communicate()
now = datetime.now().strftime("%d.%m.%Y %H:%M")
print(f"Done at {now}" )
sendMessageToGroup(f"{hostname}: plotting done on {now}")