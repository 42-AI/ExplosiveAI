from bomberman						import defines
from bomberman.defines				import t_action


from ExampleAgents.bob.coordinates.get_coordinates import (
	get_new_coordinates,
	get_all_bomb_coordinates,
	get_blasts_coordinates,
	get_accessible_coordinates,
)

from ExampleAgents.bob.coordinates.is_coordinates import (
	is_valid_coordinates, 
	is_safe_coordinates, 
	is_walkable_coordinates
)

from typing import List, Tuple, Union

Coordinates = Union[Tuple[int, int], Tuple[float, float]]

class Node():
	def __init__(self, coordinates: Coordinates, history: List[t_action], ends: List[Coordinates]) -> None:
		self.coordinates = coordinates
		self.history = history
		self.ends = ends

	def get_childs(self, board: List[List[str]], walkable=True):
		childs = []
		for action in defines.move_space:
			coordinates = get_new_coordinates(self.coordinates, action)
			is_ok = is_walkable_coordinates if walkable else is_valid_coordinates
			if is_ok(board, coordinates):
				history = self.history + [action]
				child = Node(coordinates, history, self.ends)
				childs.append(child)
		return childs

	def is_over(self):
		if self.coordinates in self.ends:
			return True
		return False

	def cost(self):
		c = self.coordinates
		h = len(self.history)
		lens = [abs(c[0] - x) + abs(c[1] - z) for x, z in self.ends]
		return h + min(lens)
	
	def __eq__(self, __o: object) -> bool:
		if self.coordinates == __o.coordinates:
			return True
		return False

class A_Star():
	def __init__(self, board):
		self.board = board
		self.big_queue = []

	def launch_Astar(self, begin, ends, walkable=True):
		def tt_cost(x): return x.cost()

		self.big_queue = [Node(begin, [], ends)]

		while len(self.big_queue):
			node = self.big_queue.pop(0)
			childs = node.get_childs(self.board, walkable)
			for child in childs:
				if child.is_over():
					return child.history
				if not child in self.big_queue:
					self.big_queue.extend(childs)
			self.big_queue.sort(key=tt_cost)

