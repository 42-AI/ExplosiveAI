from dataclasses import dataclass
from typing import List

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

	def __str__(self):
		repr_dict = {
			"1": "1️⃣ ",
			"2": "2️⃣ ",
			"B": "💣",
			"E": "💥",
			"W": "🧱",
			"C": "📦",
			"r": "📏",
			"b": "🎒",
			"s": "🏃‍♀️",
			" ": "  ",
		}

		msg = f""
		for line in self.board:
			for block in line:
				msg += f"{repr_dict[block]} "
			msg += f"\n"
		return msg