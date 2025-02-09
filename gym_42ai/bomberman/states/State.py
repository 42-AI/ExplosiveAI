from dataclasses import dataclass, field

from typing import List, Tuple
from typing import Dict

from bomberman.states.StatePlayer import StatePlayer
from bomberman.states.StateBoard import StateBoard

from colorama import Back

from .. import defines

@dataclass
class State:
	raw_board: 	List[List[str]]
	board: 		StateBoard = field(init=False)
	players: 	List[StatePlayer]
	winner: 	bool


	def __post_init__(self):
		self.board = StateBoard(self.raw_board)


	def as_tuple(self) -> Tuple[List[List[str]], List[StatePlayer], bool]:
		"""Returns a (board, players, winner) tuple
		
		board is an array of size (11, 11) containing the following strings
			Player1		: "1",
			Player2		: "2", 
			Bomb		: "B", 
			Explosion	: "E", 
			Wall		: "W", 
			Crate		: "C", 
			Bomb explosion Range Bonus 	: "r", 
			Extra Bomb Count Bonus		: "b", 
			Extra Speed Bonus			: "s"

		players is an array of json objects representing the players
			
		winner is None if no one has won yet, otherwise it is 1 or 2
		"""

		# pp = []
		# for p in players:
		# 	pp.append(StatePlayer(p, self.player_num))
		return self.board.board, self.players, self.winner


	def __str__(self):
		msg = f""
		player_missing_fix = [self.players[x] if x < len(self.players) else None for x in range(defines.NUM_PLAYERS)]
		# This fixes the out of bounds in case of dead or missing players in the line below 
		s_board = self.board.str_with_back(player_missing_fix[0], player_missing_fix[1])
		msg += f"{s_board}\n"
		msg += f"{player_missing_fix[0]}\n"
		msg += f"{player_missing_fix[1]}\n"
		msg += f"{self.winner = }\n"
		return msg