import time

from bomberman.Environment import Environnement
from numpy import true_divide


if __name__ == "__main__":
	from bomberman.agents.RandomAgent	import RandomAgent
	from bomberman.states.State			import State
	from ExampleAgents.NoSuicide 		import NoSuicide
	from ExampleAgents.bob.Agent 		import BobAgent

	# We connect to the game
	game_connection = Environnement(player_num=2)

	# We wait for both players to Be connected
	game_connection.client.wait_everyone_ready()

	# We create our agent (the algorithm that plays the game)
	agent 		= BobAgent(player_num=2)

	# We get the initial state of the game
	state 		= game_connection.get_state()
	game_over 	= False

	while game_over != True:
		# We give the agent the state of the game and he chooses an action to take
		action 	= agent.get_action(state)

		# We send the action to the game and recieve the new state
		state 	= game_connection.do_action(action)


		if (state.winner is not None):
			game_over = True
			print(f"The winner is {state.winner}")


