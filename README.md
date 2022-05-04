# Explosive AI

![Bob Agent Demo](./assets/Demo_Bob.gif)

This is a client to control a player in a BomberBuddy game. The purpose is to have a competition where AI agents and algorithms try to blow each other up! However this project is in beta and probably has some bugs so please raise an issue or send me a message on the 42 slack (jbarment or ldevelle).  

<br/>


- [Explosive AI](#explosive-ai)
	- [How it works](#how-it-works)
		- [Requirements](#requirements)
		- [Download the game](#download-the-game)
		- [Install the Package](#install-the-package)
		- [FIGHT !](#fight-)
	- [How you can help ?](#how-you-can-help-)
	- [Thanks](#thanks)


<br/>

## How it works

### Requirements
You need to have Python 3.8, if not ask google how to get it.

Clone the repo

```sh
git clone https://github.com/42-AI/ExplosiveAI.git
cd ExplosiveAI
```

Install some dependencies

```sh
python3.8 -m pip install --upgrade pip
python3.8 -m pip install build
```

### Download the game

First you need to download the game

- mac: [https://drive.google.com/file/d/1F5GoeN_-0d1NlI7jnxCjBKJHthOO0Bk1](https://drive.google.com/file/d/1F5GoeN_-0d1NlI7jnxCjBKJHthOO0Bk1)

- Linux: [https://drive.google.com/file/d/19j9jLHTMItYzpvW5AvbufL0z1VLRaVST](https://drive.google.com/file/d/19j9jLHTMItYzpvW5AvbufL0z1VLRaVST)

<details>
  <summary>
        Google-Drive folder with all the versions:
  </summary>
[https://drive.google.com/drive/folders/1kj8vKwkhwvW7axFQb2WgCxjInvUP-KRc?usp=sharing](https://drive.google.com/drive/folders/1kj8vKwkhwvW7axFQb2WgCxjInvUP-KRc?usp=sharing)
</details>


Then you need to extract it under the directory `simulator` in this project directory. So that the structure looks like this

```
ExplosiveAI
└── simulator
    └── build
        ├── bomber_Data
        ├── bomber.x86_64
        ├── LinuxPlayer_s.debug
        ├── UnityPlayer_s.debug
        └── UnityPlayer.so
```

Finnaly you can had the executable rights

```sh
chmod +x simulator/build/bomber.x86_64
```

<br/>

### Install the Package

**If you already installed the package** you may want to start by running:

```sh
pip uninstall bomberman 
```

You may now build the wheel (the type of file that pip uses to install a package)

```sh
python3.8 -m build 
```

You may now install our ***beautiful*** package

```sh
python3.8 -m pip install dist/bomberman-0.1.0-py3-none-any.whl
```

<br/>


### FIGHT !

You can now ***start the game*** and run fight.py with python3.

```sh
python3.8 fight.py
```

The code to `NoSuicide/Agent.py` contains what you need to know to start building an agent.  

<br/>

## How you can help ?

You can help by reporting bugs or suggesting features / improvements.  

Don't be shy to say something looks wierd or stupid or to ask for stuff.

If you want to help dev on the project contact us at contact@42ai.fr.  

<br/>

## Thanks
Thank you for participating in the beta of this project and helping 42AI organize cool competitions in the school
