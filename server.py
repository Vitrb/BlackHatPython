import socket
import threading

IP = "0.0.0.0"
PORT = 1000

def main():
	
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((IP,PORT))
	server.listen(5)
	print (f"\n[*] Listening on {IP}:{PORT}")
	
	while True:
		
		client,address = server.accept()
		print (f"[*] Connection accepted from {address[0]}:{address[1]}")
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()

def handle_client(client_socket):
	with client_socket as s:
		response = s.recv(1024)
		print (f"[*] Received: {response.decode('utf-8')}")
		s.send(b"ACK")


if __name__ == "__main__":

	main()
