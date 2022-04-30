from gym.agents.BaseAgent import BaseAgent
from random import Random
from gym import defines, Environment


class RandomAgent(BaseAgent):
	def __init__(self, player_num):
		self.player_num = player_num
		print("I Am a random agent, please help me get smarter than this !")

	def get_action(self, state):
		"""
			This is where you put something smart to choose an action.

			Returns
			-------
			action   : int
				The action you think we should do based on the state. (for example defines.Bomb)
		"""
		return (Random().choice(defines.action_space))
