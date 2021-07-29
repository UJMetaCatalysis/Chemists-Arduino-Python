# Chemists-Arduino-Python

This is a repository of the libraries required to install and use the Commanduino system for controlling Arduino boards.
Commanduino allows a PC running Python scripts (another name for Python programs) to control an Arduino board using a USB cable. 

For the Arduino to understand the instructions sent by the Python scripts, we need to set up software for both sides:
Python side: "commanduino"
Arduino side: "Arduino-CommandTools" and "CommandHandler". 

Once this is all set up, we can write Arduino sketches (another name for Arduino programs) that allow the Arduino to understand the Python scripts.

## Installation
Instructions for installing the software can be found each corresponding folder here on the repository. Just click on the folder and scroll down to the readme section.
Before installing the software, it is recommended that you install Python and the Arduino IDE (integrated development environment)

### Installing Python
Go to: https://www.python.org/downloads/ and download the installer for your operating system. 
Run the installer. At the bottom of the window, tick "Add Python X.X to PATH". Then select "Install Now". 

### Installing Arduino IDE
Download the installer from: https://www.arduino.cc/en/software.

## Using the command prompt/terminal
For Windows users, you access the command prompt by searching for "Command Prompt" and opening the corresponding app. To enter a command, type it into the window and press
enter. Here are some basic commands to get you started:
*cd*                      - change directory. Type cd followed by the directory name to move to that directory. Pressing Tab while typing the directory name will autocomplete the name.
*cd ..*                   - change directory to the parent directory. Useful for going back.
*dir*                     - displays the content of the current directory.
*python script_name.py*   - runs script_name.py using python. You should be in the directory where the script is stored (use cd to get there)

For Mac or Linux users, you access the terminal by searching for it and opening the corresponding app. To enter a command, type it into the window and press
enter. Here are some basic commands to get you started:

*cd*                      - change directory. Type cd followed by the directory name to move to that directory. Pressing Tab while typing the directory name will autocomplete the name.
*cd ..*                   - change directory to the parent directory. Useful for going back.
*ls*                      - displays the content of the current directory.
*python script_name.py*   - runs script_name.py using python. You should be in the directory where the script is stored (use cd to get there)

In the readme's of the software, you may see blocks like this:
```shell
This is a code block, generally it means you should type these commands
into your command prompt/terminal
```

