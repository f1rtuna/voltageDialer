# Voltage Dialer
Script Utilizing VPython to create 3d image of a voltage dial based on actual voltage recieved from potentiometer hooked up to Arduino. Potentiometer values from Arduino passed to Pythohn via serial port. Data then utilized to create a visualization to match potentiometer dial.

# Dialer in Action
https://github.com/f1rtuna/voltageDialer/assets/59737277/480263d3-027d-4ec5-9458-557e789c6fdd


# Tools
1. Arduino Uno R3
2. Potentiometer
3. Jumper Wires
4. Python Environment (really any computer with python ex. Raspberry Pi, Desktop, etc.)

# Schematic
![Screenshot 2023-12-09 at 5 44 08 PM](https://github.com/f1rtuna/voltageDialer/assets/59737277/b1ce94c9-c499-4c2f-af31-319946ed18d6)

First be sure to follow schematic when setting up Potentiometer. I've utilized the A0 pin to read in input values but feel free to use any other analog input pin you desire. Simply modify the potentPin in the voltInoPass.c file to relfect the analog input pin you use.

# Python
1. First as with any python program crete a virtual environment to house the libraries we will need (ex. serial, vpython):
   
   ```python -m venv /path/to/new/virtual/environment```

2. install the libraries from the requirements.txt file after the virtual environment you created has been activated:

   ```pip install requirements.txt```

3. Finally simply run the program once your potentiometer has been set up with your Uno:

  ```python3 voltDialer.py```

AND VOILA!:
![Screenshot 2023-12-09 at 5 54 12 PM](https://github.com/f1rtuna/voltageDialer/assets/59737277/19144bdf-a104-4358-8643-93785a17c1df)
