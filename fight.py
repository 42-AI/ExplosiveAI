import time

from gym.Environment import Environnement



class Fight():
	def __init__(self, Agent_1, Agent_2) -> None:
		self.agent_1 = Agent_1(1)
		self.env_1 = Environnement(1)

		self.agent_2 = Agent_2(2)
		self.env_2 = Environnement(2)


	def fight(self):
		self.env_1.reset()
		state_1 = self.env_1.get_state()

		self.env_2.reset()
		state_2 = self.env_2.get_state()

		game_over = False
		while game_over == False:
			time.sleep(0.1)

			# Player 1
			action_1 = self.agent_1.get_action(state_1)
			state_1 = self.env_1.do_action(action_1)

			# Player 2
			action_2 = self.agent_2.get_action(state_2)
			state_2 = self.env_2.do_action(action_2)

			_, _, w = state_2
			if (w is not None):
				game_over = True

		print(f"the winner is Player {w}")

if __name__ == "__main__":
	from gym.agents.RandomAgent import RandomAgent

	fff = Fight(RandomAgent, RandomAgent)
	fff.fight()
