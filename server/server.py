import socket
import threading
import sys

s = socket.socket()                      # Tworzenie socketu

port = 12345                             # Rezerwacja portu
s = socket.socket()
s.bind(('0.0.0.0', port))

s.listen(5)                              # Czekamy na połączenie z klientem

def processMessages(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data: 
                conn.close()
            print(data.decode("utf-8"))
            conn.sendall(bytes('Polaczenie udane', 'utf-8'))
        except:
            conn.close()
            print("Polaczenie zamkniete przez", addr)
            sys.exit()


while True:
    # Czekamy na połączenie
    print('czekam na polaczenie',flush=True)
    conn, addr = s.accept()
    print('Polaczenie od ', addr[0], '(', addr[1], ')')
    # Nasłuchujemy wiadomości
    listener = threading.Thread(target=processMessages, args=(conn, addr))
    listener.start()