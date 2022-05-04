from typing import NewType

################################################################################
# Actions                                                                      #
################################################################################

t_action = NewType('t_action', int)

# ! these are the values you put in do_action()
Nothing 	= t_action(0)
Up      	= t_action(1)
Down   		= t_action(2)
Left   		= t_action(3)
Right  		= t_action(4)     
Bomb   		= t_action(5)
Reset  		= t_action(6)
ReadyCheck	= t_action(7)

# this might be useful
move_space = [Up, Down, Left, Right]
action_space = move_space + [Nothing, Bomb]


################################################################################
# Colors                                                                       #
################################################################################

class Colors:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	RESET = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

colors = Colors()



################################################################################
# TCP Client                                                                   #
################################################################################

# this is TCP client stuff and doesnt really concern you :)
Untyped 	= 0
Player  	= 1
Controller 	= 2

dic_item_type_to_str = {
	0 : "1",
	1 : "2",
	2 : "B",
	3 : "E",
	4 : "W",
	5 : "C",
	6 : "r",
	7 : "b",
	8 : "s"
}

PATH_TO_BOMBER  = "simulator/build/bomber.x86_64"

# The server's hostname or IP address
HOST 			= "localhost"

# The port used by the server
PORT 			= 13000

# If the program must start the bomberbuddy it will wait this many seconds 
# for bomberbuddy to start before attempting to connect
SLEEP_TIME		= 5.0

################################################################################
# GLOBALS                                                                      #
################################################################################

NUM_PLAYERS		= 2