from bomberman.agents.BaseAgent		import BaseAgent
from bomberman.states.State			import State
from bomberman.defines				import t_action
from bomberman						import defines

from bomberman.states.StatePlayer	import StatePlayer
from typing import List, Tuple

from ExampleAgents.bob.utils import (
	get_players,
	move_from_to,
)
from ExampleAgents.bob.coordinates.get_coordinates import (
	get_new_coordinates,
	get_all_bomb_coordinates,
	get_blasts_coordinates,
	get_accessible_coordinates,
)

from ExampleAgents.bob.A_Star import A_Star

class BobAgent(BaseAgent):
	def __init__(self, player_num: int) -> None:
		super().__init__(player_num)
		

	def _move_to_enemy(self, 
			board: List[List[str]],
			me: StatePlayer,
			it: StatePlayer
		) -> t_action:
		action = defines.Nothing

		a_star = A_Star(board)
		solution = a_star.launch_Astar(
			begin=me.get_position(), 
			ends=[it.get_position()],
			walkable=False
		)
		if solution:
			action = solution[0]
		x, z = get_new_coordinates(
			coordinates=me.get_position(),
			action=action
		)

		# If we are blocked by Crate we place a bomb
		if board[z][x] == "C":
			action = defines.Bomb

		return action


	def _avoid_dying(self, me, board, blast_radius):
		action = defines.Nothing

		coordinates = me.get_position()
		bombs = get_all_bomb_coordinates(board)
		blasts = get_blasts_coordinates(board, bombs, blast_radius)

		if coordinates in blasts:
			accessible_coords = get_accessible_coordinates(board, coordinates)
			safe_places = [c for c in accessible_coords if not c in blasts]
			if len(safe_places):
				a_star = A_Star(board)
				solution = a_star.launch_Astar(
					begin=coordinates, 
					ends=safe_places,
					walkable=True,
				)
				if solution:
					action = solution[0]
		return action
	

	def _get_bomb_range(self, pp):
		if pp[0].bombRange > pp[1].bombRange:
			bomb_range = pp[0].bombRange 
		else:
			bomb_range = pp[1].bombRange 
		return bomb_range


	def get_action(self, state: State) -> t_action:
		"""Choose an action from a given state

		This is where you put something smart to choose an action.

		Args:
		-------
			state (State): State object from the client/Environment

		Returns:
		-------
			int:	Agent action
					It must be one the action defined in bomberman.defines

					For example:
						from bomberman import defines
						return defines.Bomb
		"""
		(board, pp, winner) = state.as_tuple()
		me, it = get_players(pp)
		blast_radius = self._get_bomb_range(pp)

		action = self._avoid_dying(me, board, blast_radius)
		if action == defines.Nothing:
			action = self._move_to_enemy(board, me, it)

		return action

