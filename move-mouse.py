import pyautogui
import time
import sys
from datetime import datetime

# returns the current time formatted as HH:MM am/pm
def printTime(message):
    currentTime = datetime.now()
    outputTime = currentTime.strftime("%I:%M %p")
    print(outputTime + ' - ' + str(message))
    

pyautogui.FAILSAFE = False
MAX_CYCLES = 180            # stop program after 180 cycles

# default sleep interval to 1 minute
numMin = 1  
if ((len(sys.argv) == 2) and (sys.argv[1].isnumeric) and (sys.argv[1] >= 1)):
    numMin = sys.argv[1]

# print program data
print()
printTime('Program started')
print('Sleep cycle: ' + str(numMin) + ' min.\n')


for numCycles in range(MAX_CYCLES):
    # make program sleep for specified sleep cycle
    for count in range(numMin):
        time.sleep(60)

    # slightly move mouse
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 1, y + 1)

    # pyautogui.press("shift")

    # report time of movement
    printTime('Mouse moved.')