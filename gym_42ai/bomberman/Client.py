from ctypes import sizeof
import math
import socket
import json
import os
import logging
import os
import subprocess
import time


import colorama
from colorama import Fore
from matplotlib.pyplot import delaxes

from bomberman						import defines
from bomberman.states.State			import State
from bomberman.states.StatePlayer	import StatePlayer
from bomberman.defines				import t_action


def get_item_position(item):
	return round(item["position"]["x"]), round(item["position"]["z"])


class  Client():
	'''
		This is the class that actually connects to the bomber game
	'''
	def __init__(self, player: int):
		self.board			= []
		self.h 				= 11
		self.w 				= 11
		self.msg 			= ""
		self.player 		= player
		self.player_states	= []
		self.connected		= False
		self.winner			= None

		for i in range(self.h):
			self.board.append([([" "] * (self.w))])
		

	def connect(self):
		print("CONNNNECTING\n\n\n\n")
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((defines.HOST, defines.PORT))
			self.connected = True
		except:
			subprocess.Popen([defines.PATH_TO_BOMBER])
			time.sleep(defines.SLEEP_TIME)
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.connect((defines.HOST, defines.PORT))
			self.connected = True
		print("CONNNNECTEEED\n\n\n\n")
			
		
	def request_type(self, num:int = -1, typo = defines.Player ,passw = "default"):
		'''_summary_

		Args:
			num (int, optional): Requested player number, -1 (first available) only works if player not instantiated. Defaults to -1.
			typo (_type_, optional): requested type of connection, relates to some game-side server stuff. Defaults to defines.Player.
			passw (str, optional): password to connect, not implemented for now. Defaults to "default".
		'''
		msg = {"requestedType" : typo, "pass" : passw, "playerNum" : num}
		self.send_msg(msg)
		self.recv_msg()
		self.parse_request()


	def wait_everyone_ready(self):
		while (True):
			time.sleep(0.05)
			msg = {"action" : defines.ReadyCheck, "playerNum" : self.player, "pass": "lolpas"}
			self.send_msg(msg)
			self.recv_msg()
			print("msg; ", self.msg)
			res = json.loads(self.msg)
			if (res["ready"] == True):
				break;
		self.send_action(defines.Nothing)


	def close(self):
		self.sock.close()


	def send_msg(self, msg):
		# if (self.sock.)
		data = json.dumps(msg)
		# print("Sending: ", data)
		self.sock.sendall(bytes(data,encoding="utf-8"))
		# print("Sent\n\n")


	def recv_msg(self):
		self.msg = ""
		n = int(self.sock.recv(8))
		while (n > 0):
			received = self.sock.recv(4096)
			received = received.decode("utf-8")
			self.msg += received
			n = n - len(received)

	
	def parseboard(self, msg):
		self.board			= []
		self.player_states	= []
		self.winner			= None

		for i in range(self.h):
			self.board.append(([" "] * (self.w)))
		
		array_of_all_items = json.loads(msg)
		for item in array_of_all_items:
			if (item["type"] == -1):
				self.winner = item["winner"]
				continue;
			
			x, y = get_item_position(item)
			item_type = item["type"]
			if item.get("is_player", False) == False:
				self.board[y][x] = defines.dic_item_type_to_str[item_type]

			if item.get("is_player", False) == True:
				self.player_states.append(item)


	def printboard(self):
		for i in range(self.h):
			print(self.board[self.h - 1 - i])


	def parse_request(self):
		rep = json.loads(self.msg)
		if (rep["requestedType"] == defines.Untyped):
			print("request denied")
			return
		
		self.player = rep["playerNum"]


	def send_action(self, action: t_action, print_state_to_terminal = True):
		msg = {"action" : action, "playerNum" : self.player, "pass": "lolpas"}
		self.send_msg(msg)
		self.recv_msg()
		self.parseboard(self.msg)


	def reset(self):
		self.winner = None
		self.send_action(defines.Reset)

	
	def get_state(self) -> State:
		'''
		Returns
		-------
		state: State
			board   : StateBoard
				board.board is an array of strings of size (11, 11) representing the board, 
				player positions are rounded to the grid, 
				for exact positions refer to the players array

			players : array
				array of PlayerState objects representing the players

			winner   : int
				1, 2 or None if game is not over.

		Notes
		-----
			UNDERSTANDING THE BOARD ARRAY
			Here are the strings and what they represent:
			Player1		: "1",
			Player2		: "2", 
			Bomb		: "B", 
			Explosion	: "E", 
			Wall		: "W", 
			Crate		: "C", 
			Bomb explosion Range Bonus 	: "r", 
			Extra Bomb Count Bonus		: "b", 
			Extra Speed Bonus			: "s"
		'''
		pp = []
		for p in self.player_states:
			pp.append(StatePlayer(p, self.player))
		s = State(self.board, pp, self.winner)
		return s
