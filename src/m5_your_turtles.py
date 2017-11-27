"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Patrick Vedova.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
pacman = rg.SimpleTurtle('turtle')
pacman.pen = rg.Pen('yellow',10)
blinkie = rg.SimpleTurtle('turtle')
blinkie.pen = rg.Pen('blue',5)
pacman.speed = 5
blinkie.speed = 4
size = 100
for n in range(20):
    pacman.draw_regular_polygon(8, 50)
    pacman.pen_up()
    pacman.right(45)
    pacman.forward(10)
    pacman.left(45)
    pacman.pen_down()
    blinkie.draw_regular_polygon(7, 50)
    blinkie.pen_up()
    blinkie.right(45)
    blinkie.forward(25)
    blinkie.left(45)
    blinkie.pen_down()



