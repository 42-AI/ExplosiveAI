# Algorithms with bombs

This is a client to control a player in a BomberBuddy game. The purpose is to have a competition where AI agents and algorithms try to blow each other up! However this project is in beta and probably has some bugs so please raise an issue or send me a message on the 42 slack (jbarment).    

## How it works

Download the game and put the path to the game in Client.py
mac:   
https://drive.google.com/file/d/1F5GoeN_-0d1NlI7jnxCjBKJHthOO0Bk1/view?usp=sharing

Linux:   
https://drive.google.com/file/d/19j9jLHTMItYzpvW5AvbufL0z1VLRaVST/view?usp=sharing

```python
PATH_TO_BOMBER = "/home/me/bomber.x86_64"
```

run fight.py with python3.  

```bash
cd src
python3 fight.py "./ExampleAgent.py" "./ExampleAgent.py" 
python3 fight.py "./ExampleAgent.py" "./ExampleAgent.py" fast
```

if you do not want to relaunch the game everytime use the fast option.

```bash
python3 fight.py "./ExampleAgent.py" "./ExampleAgent.py" fast
```

The code to ExampleAgent.py contains what you need to know to start building an agent.  
use fight.py to make two agents fight.

## How you can help ?

You can help by reporting bugs or suggesting features / improvements.  
Don't be shy to say something looks wierd or stupid or to ask for stuff (i.e I wanna be able to play against my AI)  
If you want to help dev on the project contact us at contact@42ai.fr.  

## Thanks

Thank you for participating in the beta of this project and helping 42AI organize cool competitions in the school