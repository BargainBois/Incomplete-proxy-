import socket, sys
from thread import *
try:
    listening_port = int(raw_input("[*] Enter Port Number: "))
except KeyboardInterrupt:
        print ("\n[*] User Requested An Interrupt")
        print ("[*] Application Exiting ...")
        sys.exit()
        max_conn = 5 #Holds connection
        buffer_size = 8192 #max size      
 def start():      
     try:
         s = socket.socket(socket.AF_INET, socket.SOCK_stream)
         s.bind(('',listening_port))
         s.listen(max_conn)
         print "[*] Starting Sockets... Done"
         print "[*] sockets Binded..."
         print("[*] server Started [ %d ]\n" % (listening_port))
    except Exeception, e:
        print "[*] Unable to start Socket"
        sys.exit(2)

    while 1:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            start_new_thread(conn_string, (conn,data, addr))
        except KeyboardInterrupt:
            s.close()
            print"\n[*] Proxy Server Shutting Down ..."
            sys.exit(1)

if (len(reply) > 0):
                  conn.send(reply)
                  dar = float(len(reply))
                  dar = float(dar / 1024)
                  dar ="%.3s" % (str(dar))
                  dar ="%s KB" % (dar)
                  print"Request complete"
                  print "[*] Request Done: %s => %s <=" % (str(addr[0]),str(dar))
else: break
        s.close()
        conn.close()
except socket.error, (value, message):
            s.close()
            conn.close()
            sys.exit(1)
            start()

                  
                  
