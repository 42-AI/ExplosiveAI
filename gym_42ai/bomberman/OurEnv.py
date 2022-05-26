from bomberman.Client 				import Client
from bomberman.defines				import t_action
from bomberman 		 				import defines
from bomberman.states.State			import State

import gym
from gym import spaces
import numpy as np
from typing import Optional
from gym.utils.renderer import Renderer

# - Position est int et la move speed est float? Lequel est correst?
# - Ca veut dire quoi player_num=-1?
# - Est-ce que c'est prevu d'integrer plus de 2 joueurs?
# - Comment fonctionne le passage en mode headless? Est-ce qu'on peut avoir une fonction render?


class Bomberman(gym.Env):
    metadata = {
        "render_modes": ["human", "rgb_array"],
        "render_fps": 4
    }

    def __init__(self, player_num: int = -1):
        '''
		player_num is the number of the player we want to be (1 or 2) put -1 for any available number.
		'''
        if player_num == -1 :
            player_num = 2

		self.client = Client(player_num)
		self.client.connect()
		self.client.request_type(player_num, defines.Player)
		self.client.send_action(defines.Nothing)
		self.player_num = self.client.player

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        board_state_space = spaces.MultiDiscrete(np.full((12, 12), 7 + player_num))
        player_state_space = spaces.Dict({
            "moveSpeed": spaces.Box(low=4.0, shape=(1,), dtype=np.float32) #NOTE: unclear
            "bombAmount": spaces.Box(low=0, shape=(1,), dtype=int)
            "bombRange": spaces.Discrete(low=2, shape=(1,), dtype=int)
            "position": spaces.MultiDiscrete([12,12]) # (x, z) - redondant
            "isDead": spaces.Discrete(2) #bool
        })
        obv_space_dict = {"board":board_state_space}
        for i in range(player_num):
            obv_space_dict["player" + str(i)] = player_state_space
        self.observation_space = spaces.Dict(obv_space_dict)

        # We have 6 actions per player, corresponding to "go right", "go up", "go left", "go down", "place bomb", "do nothing"
        player_action_space = spaces.Discrete(6)
        act_space_dict = {}
        for i in range(player_num):
            act_space_dict["player" + str(i)] = player_action_space
        self.action_space = spaces.spaces.Dict()


        # """
        # If human-rendering is used, `self.window` will be a reference
        # to the window that we draw to. `self.clock` will be a clock that is used
        # to ensure that the environment is rendered at the correct framerate in
        # human-mode.
        # """
        # if render_mode == "human":
        #     import pygame  # import here to avoid pygame dependency with no render

        #     pygame.init()
        #     pygame.display.init()
        #     self.window = pygame.display.set_mode((self.window_size, self.window_size))
        #     self.clock = pygame.time.Clock()
                
        # # The following line uses the util class Renderer to gather a collection of frames 
        # # using a method that computes a single frame. We will define _render_frame below.
        # self.renderer = Renderer(render_mode, self._render_frame)
