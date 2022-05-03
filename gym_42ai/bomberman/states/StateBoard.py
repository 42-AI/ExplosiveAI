from dataclasses import dataclass
from typing import List
from bomberman.states.StatePlayer import StatePlayer
from colorama import Back

@dataclass
class StateBoard:
	"""StateBoard
	
	StateBoard.board is an array of size (11, 11)

	It contains the following objects with string representation:

		Player1		: "1",
		Player2		: "2", 
		Bomb		: "B", 
		Explosion	: "E", 
		Wall		: "W", 
		Crate		: "C", 
		Bomb explosion Range Bonus 	: "r", 
		Extra Bomb Count Bonus		: "b", 
		Extra Speed Bonus			: "s"
	"""
	board: List[List[str]]

	def str_with_back(self, player_1: StatePlayer=None, player_2: StatePlayer=None):
		p_1 = player_1.get_position() if player_1 else (-1, -1)
		p_2 = player_2.get_position() if player_2 else (-1, -1)
		repr_dict = {
			"1": "1️⃣ ",
			"2": "2️⃣ ",
			"B": "💣",
			"E": "💥",
			"W": "🧱 ",
			"C": "📦",
			"r": "📏",
			"b": "🎒",
			"s": "👟",
			" ": "  ",
		}

		msg = f""
		# X indices
		msg += f" "
		for x, line in enumerate(self.board):
			msg += f"  {x}"
		msg += f" 👉 x\n"
		# Board
		for z, line in enumerate(self.board):
			msg += f"{z:<3}"
			for x, block in enumerate(line):
				coord = (x, z)
				if p_1 == coord:
					msg += f"{Back.RED}"
				if p_2 == coord:
					msg += f"{Back.BLUE}"
				msg += f"{repr_dict[block]}"
				if p_1 == coord or p_2 == coord:
					msg += f"{Back.RESET}"
				msg += f" "
			msg += f"\n"
		msg += f"👇\n"
		msg += f" z\n"

		return msg

	def __str__(self):
		return self.str_with_back()