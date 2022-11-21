import socket
import sys
import time
import datetime
import pymssql

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('ip address', 2305)
    print(sys.stderr, 'connecting to %s port %s' % server_address)
    try:
        sock.connect(server_address)
        try:
            print(sys.stderr, 'connecting success')
            while True:
                data = sock.recv(16)
                y = str(data).split(' ')
                data2 = y[2]
                x = data2[0:-1]
                try:
                    newdate = datetime.datetime.now()
                    d1 = newdate.day
                    m1 = newdate.month
                    y1 = newdate.year
                    h1 = newdate.hour
                    i1 = newdate.minute
                    conn = pymssql.connect("ip address server","username","password","database")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO weight_tb_test (value,...) VALUES (type value,...)",
                    "data.....")
                    conn.commit()
                    conn.close()
                    print(sys.stderr, 'query success received "%s"' % x)
                except Exception as e:  
                    print(e)
                    conn.close()  
                if len(data) < 1:
                    break
        finally:
            print(sys.stderr, 'closing socket')
            sock.close()
    except:
        print("An exception occurred try again in 5 second")
        time.sleep(5)