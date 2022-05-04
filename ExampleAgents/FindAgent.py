from bomberman.agents.BaseAgent		import BaseAgent
from bomberman.states.State			import State
from bomberman.defines				import t_action
from bomberman						import defines

from bomberman.states.StatePlayer	import StatePlayer
from typing import List

def get_players(pp: List[StatePlayer]):
	if pp[0].enemy:
		me, yu = pp[1], pp[0]
	else:
		me, yu = pp[0], pp[1]
	return me, yu


class FindAgent(BaseAgent):
	def __init__(self, player_num: int) -> None:
		super().__init__(player_num)
		

	def _direction_to_enemy(self, mine: StatePlayer, their: StatePlayer) -> t_action:
		diff_horizontal = mine.x - their.x
		diff_vertical = mine.z - their.z

		if abs(diff_horizontal) > abs(diff_vertical):
			if diff_horizontal > 0:
				action = defines.Down
			else:
				action = defines.Up
		else:
			if diff_vertical > 0:
				action = defines.Right
			else:
				action = defines.Left
		
		return action


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
		st = state.as_tuple()
		(s, pp, w) = st
		mine, their = get_players(pp)
		action = self._direction_to_enemy(mine, their)
		return action

