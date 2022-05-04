from bomberman.agents.BaseAgent		import BaseAgent
from bomberman.states.State			import State
from bomberman.defines				import t_action
from bomberman						import defines

from random import Random

class NoSuicide(BaseAgent):
	def __init__(self, player_num: int) -> None:
		super().__init__(player_num)


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
		return (Random().choice(defines.move_space))
