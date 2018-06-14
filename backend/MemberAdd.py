#Regystration script for the Reference Database
import socket
import time
HOST_IP = "127.0.0.1"
HOST_PORT = 4005

def main():
	ReceiverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Server_Addr = (HOST_IP, HOST_PORT)
	ReceiverSocket.bind(Server_Addr)
	ReceiverSocket.listen(1)
	Tries = 0
	End_Transmission = 1
	while End_Transmission:
		connection, client_address = ReceiverSocket.accept()
		if(client_address):
			try:
				print "Recieved connection from {0}".format(client_address)
				data = connection.recv(10)
				if data:
					connection.sendall(data)
if __name__ == "__name__":
	main()
