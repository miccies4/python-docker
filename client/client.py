import socket                            # Import socket module
import time
import threading

WAIT_SECONDS = 3
port = 12345                            # Wybór portu
conn = socket.socket()                   # Tworzymy socket

conn.connect(('server', port))

conn.sendall(b'Connected. Wait for data...') 
def wysylanie():
	    intosend = ("Wiadomość")
	    conn.sendall(intosend.encode('utf-8'))
	    #Otrzymanie danych z serwerem - komunikacja
	    data = conn.recv(1024)
	    print("Data: ", data.decode('utf-8'))
	    threading.Timer(WAIT_SECONDS, wysylanie).start() 
wysylanie()                                # zamkniecie po zakończeniu