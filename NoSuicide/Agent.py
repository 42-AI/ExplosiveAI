from bomberman.agents.BaseAgent import BaseAgent
from bomberman.utils import defines

from random import Random

class Mikael(BaseAgent):
	def __init__(self, agent_number) -> None:
		super().__init__(agent_number)

	def get_action(self, state):
		"""
			This is where you put something smart to choose an action.

			Returns
			-------
			action   : int
				The action you think we should do based on the state. (for example defines.Bomb)
		"""
		return (Random().choice(defines.move_space))
