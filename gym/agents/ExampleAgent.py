from random import Random
from gym.Environment import Environnement
from gym import defines
from gym.agents import BaseAgent


class RandomAgent(BaseAgent):
	def __init__(self, player_num):
		super().__init__()
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


import sys
import time
if __name__ == "__main__":
	agent = RandomAgent(int(sys.argv[1]))
	# agent.env.reset()
	state1 = agent.get_state()
	game_over = False


	while game_over == False:
		time.sleep(0.1)
		state = agent.do_action(agent.get_action(state1))
		_, _, w = state
		if (w is not None):
			game_over = True
