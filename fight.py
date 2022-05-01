import time

from bomberman.Environment import Environnement



class Fight():
	def __init__(self, Agent_1, Agent_2) -> None:
		self.agent_1 = Agent_1(1)
		self.env_1 = Environnement(1)

		self.agent_2 = Agent_2(2)
		self.env_2 = Environnement(2)


	def fight(self):
		# Player 1
		self.env_1.reset()
		state_1 = self.env_1.get_state()

		# Player 2
		self.env_2.reset()
		state_2 = self.env_2.get_state()

		game_over = False
		while game_over == False:
			time.sleep(0.01)

			# Player 1
			action_1 = self.agent_1.get_action(state_1)
			state_1 = self.env_1.do_action(action_1)

			# Player 2
			action_2 = self.agent_2.get_action(state_2)
			state_2 = self.env_2.do_action(action_2)

			# b, pp, w = state_2
			# s = State(b, pp, w)
			print(state_2)
			if (state_2.winner is not None):
				game_over = True

		print(f"the winner is Player {w}")


import sys, inspect

def print_classes(module):
	# sys.modules[__name__]
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(obj)

if __name__ == "__main__":
	from bomberman.agents.RandomAgent	import RandomAgent
	from bomberman.states.State			import State
	from AllAgents.NoSuicide import NoSuicide
	from AllAgents.FindAgent import FindAgent
	from AllAgents.bob.Agent import BobAgent

	import importlib

	i = importlib.import_module("AllAgents.FindAgent")

	print_classes(i)

	fff = Fight(BobAgent, NoSuicide)
	fff.fight()
