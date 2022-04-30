import abc
from bomberman.utils import defines

class BaseAgent(abc.ABC):
	def __init__(self, player_num):
		self.player_num = player_num

	@abc.abstractmethod
	def get_action(self, state):
		"""
			This is where you put something smart to choose an action.

			Returns
			-------
			action   : int
				The action you think we should do based on the state. (for example defines.Bomb)
		"""
		return defines.Nothing

