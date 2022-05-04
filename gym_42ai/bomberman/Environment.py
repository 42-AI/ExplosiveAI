from bomberman.Client 				import Client
from bomberman.defines				import t_action

from bomberman 		 				import defines
from bomberman.states.State			import State

class Environnement:
	def __init__(self, player_num: int = -1):
		'''
		player_num is the number of the player we want to be (1 or 2) put -1 for any available number.
		'''
		self.client = Client(player_num)
		self.client.connect()
		self.client.request_type(player_num, defines.Player)
		# self.client.send_action(defines.Nothing)
		self.player_num = self.client.player


	def do_action(self, action: t_action) -> State:
		"""
		Takes action and Returns a (state, players, winner) tuple.

		Parameters
		----------
		action : int
			An action value defined in defines.py

		Returns
		-------
		state   : array
			An array of strings of size (11, 11) representing the board, player positions are rounded to the grid, for exact positions refer to the players array

		players : array
			array of PlayerState objects representing the players

		winner   : int
			1, 2 or None if game is not over.

		Notes
		-----
			UNDERSTANDING THE STATE ARRAY
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
		"""
		self.client.send_action(action)
		state = self.get_state()
		return state

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
		return self.client.get_state()


	def reset(self) -> State:
		self.client.reset()
		state = self.get_state()
		return state
	
