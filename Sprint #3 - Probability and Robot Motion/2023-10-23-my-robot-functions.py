from Robot373 import *

left,right=Motors("ab")
touch=Sensors("touch",None,None,None)

# I want to run the motor if the touch sensor is pressed

print("Starting...")
try:
    while True:
        if touch.value:
            left.power=50
            right.power=50
        else:
            left.power=0
            right.power=0
except KeyboardInterrupt:
    pass

print("Ending.")

Shutdown()

