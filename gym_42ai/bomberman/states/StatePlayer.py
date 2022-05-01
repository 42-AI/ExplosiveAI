from typing import Dict, Tuple
from colorama import Back

class StatePlayer:
	'''StatePlayer containing all the player information

	player_num: int
		Categorical value [-1, 1, 2]

	moveSpeed: float
		Player movement speed

	bombs: int
		Quantity of bombs the player can place at the same time

	bombRange: int
		Bomb explotion blast radius, as a rook (from chess) movements

	dead: bool
		False if player is still alive

	x: int
		The horizontal coordinate. 
		It's value is between 0 and 11 
		0 is at the left.
	
	z: int
		The vertical coordinate
		It's value is between 0 and 11 
		0 is at the bottom.

	enemy: bool
		False if it is the player controlled by the current client
	'''
	def __init__(self, json_state : Dict, num = -1):
		self.update_state(json_state=json_state)
		self.enemy		= self.player_num != num


	def update_state(self, json_state : Dict):
		self.player_num	= json_state["playerNumber"]
		self.moveSpeed 	= json_state["moveSpeed"]
		self.bombs 		= json_state["bombs"]
		self.bombRange 	= json_state["bombRange"]
		self.dead 		= json_state["dead"]
		self.x :int		= json_state["position"]["x"]
		self.z :int		= json_state["position"]["z"]


	def get_position(self) -> Tuple[int, int]:
		return round(self.x), round(self.z)

	def get_position_float(self) -> Tuple[float, float]:
		return self.x, self.z

	def __str__(self):
		indent = 5

		status = "is 💀" if self.dead else ""
		repr_dict = {
			1: "1️⃣ ",
			2: "2️⃣ "
		}

		msg = ""
		if self.player_num == 1:
			msg += f"{Back.RED}"
		elif self.player_num == 2:
			msg += f"{Back.BLUE}"
		msg += f"Player"
		msg += f"{Back.RESET}"
		msg += f" {repr_dict[self.player_num]} {status}\n"

		msg += f"{' ' * indent}"
		# msg += f"[X, Z] [{self.get_position()}], "
		msg += f"📍 {self.get_position_float()}\n"
		msg += f"{' ' * indent}"
		# msg += f"speed {self.moveSpeed}\n"
		msg += f"👟 {self.moveSpeed}\n"
		
		msg += f"{' ' * indent}"
		# msg += f"bombs {self.bombs}, "
		msg += f"🎒 {self.bombs}\n"
		msg += f"{' ' * indent}"
		# msg += f"range: {self.bombRange}\n"
		msg += f"📏 {self.bombRange}\n"
		return msg

