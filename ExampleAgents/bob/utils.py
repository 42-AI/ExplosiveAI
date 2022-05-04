
from bomberman						import defines

from bomberman.defines				import t_action
from bomberman.states.StatePlayer	import StatePlayer

from typing import List, Tuple, Union

Coordinates = Union[Tuple[int, int], Tuple[float, float]]

def get_players(pp: List[StatePlayer]):
	if pp[0].enemy:
		me, yu = pp[1], pp[0]
	else:
		me, yu = pp[0], pp[1]
	return me, yu



def move_from_to(from_: Coordinates, to_: Coordinates) -> t_action:
	diff_horizontal = from_[0] - to_[0]
	diff_vertical 	= from_[1] - to_[1]

	if abs(diff_horizontal) > abs(diff_vertical):
		if diff_horizontal > 0:
			action = defines.Down
		else:
			action = defines.Up
	else:
		if diff_vertical > 0:
			action = defines.Right
		else:
			action = defines.Left
	
	return action

