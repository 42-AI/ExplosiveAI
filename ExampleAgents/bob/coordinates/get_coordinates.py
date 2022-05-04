from bomberman						import defines
from bomberman.defines				import t_action
from bomberman.states.StatePlayer	import StatePlayer

from ExampleAgents.bob.coordinates.is_coordinates import (
	is_valid_coordinates, 
	is_safe_coordinates, 
	is_walkable_coordinates
)

from typing import List, Tuple, Union

Coordinates = Union[Tuple[int, int], Tuple[float, float]]

def get_new_coordinates(coordinates: Coordinates, action: int) -> Coordinates:
	x, z = coordinates
	if action == defines.Up:
		z += 1
	elif action == defines.Down:
		z -= 1
	elif action == defines.Left:
		x -= 1
	elif action == defines.Right:
		x += 1
	return x, z

def get_all_bomb_coordinates(board: List[List[str]]) -> List[Coordinates]:
	bombs = []
	for z, line in enumerate(board):
		for x, item in enumerate(line):
			if item == "B":
				bombs.append((x, z))
	return bombs

def get_neighbors(
	board: List[List[str]], 
	begin: List[Coordinates]
	) -> List[Coordinates]:

	neighbors = []
	distance = 1
	coords = []
	coords.append((begin[0] + distance, begin[1]))
	coords.append((begin[0] - distance, begin[1]))
	coords.append((begin[0], begin[1] + distance))
	coords.append((begin[0], begin[1] - distance))
	for coord in coords:
		if is_valid_coordinates(board, coord):
			neighbors.append(coord)

	return neighbors 


def get_blasts_coordinates(
		board: List[List[str]], 
		bombs: List[Coordinates], 
		blast_radius: int
	) -> List[Coordinates]:

	blasts = []
	for bomb in bombs:
		if not bomb in blasts:
			blasts.append(bomb)
		for distance in range(1, blast_radius):
			coords = []
			coords.append((bomb[0] + distance, bomb[1]))
			coords.append((bomb[0] - distance, bomb[1]))
			coords.append((bomb[0], bomb[1] + distance))
			coords.append((bomb[0], bomb[1] - distance))
			for coord in coords:
				if is_valid_coordinates(board, coord) and not coord in blasts:
					blasts.append(coord)
	
	# The following code is here to protect against the BIG bounding box
	ext_blasts = []
	for blast in blasts:
		coords = get_neighbors(board, blast)
		for coord in coords:
			if not coord in ext_blasts:
				ext_blasts.append(coord)

	blasts = ext_blasts
	ext_blasts = []
	for blast in blasts:
		coords = get_neighbors(board, blast)
		for coord in coords:
			if not coord in ext_blasts:
				ext_blasts.append(coord)

	return ext_blasts


def get_accessible_coordinates(
		board: List[List[str]], 
		current: Coordinates, 
	) -> List[Coordinates]:

	all_coordinates = []

	accessible_coordinates = [current]
	while len(accessible_coordinates):
		coord = accessible_coordinates.pop(0)
		for move in defines.move_space:
			new_coord = get_new_coordinates(coord, move)
			if is_walkable_coordinates(board, new_coord):
				if not new_coord in accessible_coordinates:
					if not new_coord in all_coordinates:
						accessible_coordinates.append(new_coord)
		all_coordinates.append(coord)

	return all_coordinates
