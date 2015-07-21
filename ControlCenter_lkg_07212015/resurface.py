import cmdAgent
import getPosition
def resurface():
    global tolerance
    global location

    while location[2] > tolerance:
       cmdAgent.cmdAgent(Rise)
       getPosition.getPosition()
       return 0
