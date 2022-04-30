#!/usr/bin/env bash

################################################################################
# CONSTANTS                                                                    #
################################################################################

######################################
# Colors                             #
######################################
COLOR_RED="\e[1;31m"
COLOR_GREEN="\e[1;32m"
COLOR_YELLOW="\e[1;33m"
COLOR_BLUE="\e[1;34m"
COLOR_PURPLE="\e[1;35m"
COLOR_CYAN="\e[1;36m"
COLOR_RESET="\e[0m"

######################################
# G-Drive URLS                       #
######################################
GDRIVE_URL_MAC"https://drive.google.com/file/d/1XuEEzePBdoZVaM0SrQ857k6HqccUKXn"
GDRIVE_URL_LINUX="https://drive.google.com/file/d/1zNIrXT5JbrAdudhubCN9JCn-Tn7tBxLs"

######################################
# PATHs                              #
######################################
DOWNLOAD_DIR="simulator/"
EXTRACT_PATH=$DOWNLOAD_DIR
DOWNLOAD_PATH=$DOWNLOAD_DIR"Bomberman.tar.xz"
SIMULATOR_PATH="simulator/build/bomber.x86_64"

######################################
# ERRORS                             #
######################################
ERROR_DOWNLOAD="This page checks to see if it's really a human sending the requests and not a robot"


################################################################################
# OS-CHECK                                                                     #
################################################################################
echo -e $COLOR_YELLOW "Checking OS" $COLOR_RESET 

if [ "$(uname)" == "Darwin" ]; then
	echo -e $COLOR_GREEN "Mac detected !" $COLOR_RESET
	GDRIVE_URL=$GDRIVE_URL_MAC
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
	echo -e $COLOR_GREEN "Linux detected !" $COLOR_RESET
	GDRIVE_URL=$GDRIVE_URL_LINUX
else
    echo -e $COLOR_RED "ERROR: OS " $COLOR_RESET "'"  `uname`  "'" $COLOR_RED "is not supported" $COLOR_RESET
	exit 1
fi


################################################################################
# GDOWN-CHECK                                                                  #
################################################################################
echo -e $COLOR_YELLOW "Checking if gdown is installed" $COLOR_RESET 

python3 -c 'import gdown' 1>&- 2>&-
if [ $? -ne 0 ]; then
    echo -e $COLOR_RED "ERROR: gdown is not installed" $COLOR_RESET
    echo "You can install gdown by running: "
    echo -e "> " $COLOR_YELLOW "pip install gdown" $COLOR_RESET
	exit 1
fi

echo -e $COLOR_GREEN "gdown is installed !" $COLOR_RESET


################################################################################
# SIMULATOR DOWNLOAD                                                           #
################################################################################
echo -e $COLOR_YELLOW "Downloading simulator" $COLOR_RESET

mkdir -p $DOWNLOAD_DIR
gdown $GDRIVE_URL --output $DOWNLOAD_PATH


echo -e $COLOR_YELLOW "Extracting simulator" $COLOR_RESET 

grep_output=`grep "$ERROR_DOWNLOAD" $DOWNLOAD_PATH`
if [ -n "$grep_output" ]; then
    echo -e $COLOR_RED "ERROR: google drive asked for a captcha" $COLOR_RESET
    echo "Please download the simulator manually:"
    echo -e $COLOR_YELLOW $GDRIVE_URL $COLOR_RESET
	exit 1
fi


################################################################################
# SIMULATOR ETRACT AND CHMOD                                                   #
################################################################################
tar -xvf $DOWNLOAD_PATH -C $DOWNLOAD_DIR

chmod +x $SIMULATOR_PATH

echo -e $COLOR_GREEN "Simulator is ready and here: " $COLOR_RESET $SIMULATOR_PATH
