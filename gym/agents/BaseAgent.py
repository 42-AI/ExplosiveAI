import abc

from random import Random
# from Environment import Environnement
from gym import defines

class BaseAgent(abc.ABC):
	def __init__(self, player_num):
		self.player_num = player_num

	@abc.abstractmethod
	def get_action(self, state):
		return defines.Nothing

