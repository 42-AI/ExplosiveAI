from bomberman						import defines

from bomberman.defines				import t_action
from bomberman.states.StatePlayer	import StatePlayer

from typing import List, Tuple, Union

Coordinates = Union[Tuple[int, int], Tuple[float, float]]

def is_valid_coordinates(board: List[List[str]], coordinates: Coordinates) -> bool:
	x, z = coordinates
	if not (0 <= x < 11):
		return False
	if not (0 <= z < 11):
		return False
	item = board[z][x]
	if item in ["W"]:
		return False
	return True

def is_safe_coordinates(board: List[List[str]], coordinates: Coordinates) -> bool:
	if not is_valid_coordinates(board, coordinates):
		return False
	x, z = coordinates
	item = board[z][x]
	if item in ["B", "E"]:
		return False
	return True


def is_walkable_coordinates(board: List[List[str]], coordinates: Coordinates) -> bool:
	if not is_valid_coordinates(board, coordinates):
		return False
	x, z = coordinates
	item = board[z][x]
	if item in ["C", "W"]:
		return False
	return True