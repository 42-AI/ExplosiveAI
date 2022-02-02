from ctypes import sizeof
import socket
import json
import os
import logging
import os


HOST = "localhost"  # The server's hostname or IP address
PORT = 13000        # The port used by the server

class  Client():
	def __init__(self):
		self.sim_port	= None
		self.board		= ["e"] * (19 * 19)
		self.winner		= "no"
		self.illegal	= False
		self.w_captures	= 0
		self.b_captures	= 0
		self.connected	= False

		# self.connect()
		

	def connect(self):
		print("CONNNNECTING\n\n\n\n")
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((HOST, PORT))
		self.connected = True
		

	def close(self):
		self.sock.close()


	def send_msg(self, msg):
		# if (self.sock.)
		data = json.dumps(msg)
		self.sock.sendall(bytes(data,encoding="utf-8"))
		print(f"sending {data}")


	def recv_msg(self):
		received = self.sock.recv(1024)
		print('Received', received)
		received = received.decode("utf-8")
	

		

c = Client()
c.connect()
c.send_msg({"type" : "test", "im" : "gross"})
# board = c.play_move(181)


# # c = Client()
# # c.play_game()