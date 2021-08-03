# Chemists-Arduino-Python

This is a repository of the libraries required to install and use the Commanduino system for controlling Arduino boards.
Commanduino allows a PC running Python scripts (another name for Python programs) to control an Arduino board using a USB cable. 

For the Arduino to understand the instructions sent by the Python scripts, we need to set up software for **both** the PC (running python) **AND** the Arduino (running C++):

Python side: "commanduino"

Arduino side: "Arduino-CommandTools" and "CommandHandler". 

Once this is all set up, we can write Arduino sketches (another name for Arduino programs) that allow the Arduino to understand the Python scripts.

## Installation
Instructions for installing the software can be found on each corresponding folder here on GitHub. Just click on the folder and scroll down to the readme section.
Before installing the software, it is recommended that you install Python and the Arduino IDE (integrated development environment). 

### Installing Python
Go to: https://www.python.org/downloads/ and download the installer for your operating system. 
Run the installer. At the bottom of the window, tick "Add Python X.X to PATH". Then select "Install Now". 

### Installing Arduino IDE
Download the installer from: https://www.arduino.cc/en/software.

## Installing commanduino
Open the commanduino folder on github. There are instructions on installing the software when you scroll down on that page. Don't worry about using Git, just click on the big green "Code" button, then select "Download Zip". Make sure to move that directory to somewhere other than your downloads folder. Your user folder on the PC is a good option.

## Installing Arduino-CommandTools and CommandHandler
Open the corresponding folders and follow the instructions lower down on the pages. Click on the big green "Code" button, then select "Download Zip". Move the folders to your Arduino libraries folder as per the instructions on the github page. 

## Using the command prompt/terminal
For *Windows* users, you access the *Command Prompt* by searching for "Command Prompt" and opening the corresponding app. To enter a command, type it into the window and press
enter. Here are some basic commands to get you started:


**cd**                      - change directory. Type cd followed by the directory name to move to that directory. Pressing Tab while typing the directory name will autocomplete the name.

**cd ..**                   - change directory to the parent directory. Useful for going back.

**dir**                     - displays the content of the current directory.

**python script_name.py**   - runs script_name.py using python. You should be in the directory where the script is stored (use cd to get there)


For Mac or Linux users, you access the terminal by searching for it and opening the corresponding app. To enter a command, type it into the window and press
enter. Here are some basic commands to get you started:


**cd**                      - change directory. Type cd followed by the directory name to move to that directory. Pressing Tab while typing the directory name will autocomplete the name.

**cd ..**                   - change directory to the parent directory. Useful for going back.

**ls**                      - displays the content of the current directory.

**python script_name.py**   - runs script_name.py using python. You should be in the directory where the script is stored (use cd to get there)


In the readme's of the software, you may see blocks like this:
```shell
This is a code block, generally it means you should type these commands
into your command prompt/terminal
```

## Running an example
Once you have installed all the software, you should run an example. I would recommend "CommandAccelStepper", "CommandDigitalRead", or "CommandDigitalWrite". 

1. Open the Arduino IDE
2. Go to **File->Examples** and scroll down using the arrow at the bottom of the drop-down menu. Select the desired example.
3. Make sure the Arduino is connected to the PC's USB port. 
4. Go to **Tools->Port** and select the correct port. To find the port on Windows go to Device manager and look for Ports, the format is "COMX". On Mac or Linux, open a terminal window and enter the command `ls /dev/*usb*`.
5. In the Arduino IDE, go to **Tools->Board** and make sure the board corresponds to the Arduino you are using.
6. Verify, then upload the sketch using the buttons on the top of the window. 
7. Now navigate using the file explorer to the folder where you installed the commanduino library. Open the examples folder, then "Commanddevices". Find the example that corresponds to the one you are using. 
8. Edit the .json file in the example directory to use the correct port as found in step 4
9. Open a terminal window, navigate to the folder you found in step 7 using cd, then run the example using the command `python examplename.py` where examplename is the name of the .py file you are running. 

## Common issues
### Device "XXX" not found
This can be caused by a few things:
1. You haven't set the serial port correctly in the .json file
2. You haven't set the name of the device correctly in the .json file
3. The serial port is busy/being used/isn't connected.


For 1 and 2, double check the .json file corresponding to your python script. Is the serial port named correctly under "port": "COMX" (windows) or "port": "dev/tty/etc"? Is the device name and command_id correct? The command_id should correspond **exactly** to the id you used in your Arduino sketch e.g., (cmdObj.registerToCommandManager(cmdMng, **"THIS"**)

For 3, make sure no other programs or scripts are currently using the serial port. Unplugging the USB and re-inserting it can help.


These libraries were authored by the Cronin Group at the University of Glasgow. You can find their repositories under the username "croningp" 
