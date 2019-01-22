"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Steven Kay.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(100)
blueboi = rg.SimpleTurtle('square')
blueboi.pen = rg.Pen('blue', 3)
blueboi.speed = 200
for k in range(500):
    blueboi.left(92)
    blueboi.forward(k)
redboi = rg.SimpleTurtle('square')
redboi.pen = rg.Pen('red', 3)
redboi.speed = 200
for k in range(500):
    redboi.right(92)
    redboi.forward(k)
greenboi = rg.SimpleTurtle('square')
greenboi.pen = rg.Pen('green', 3)
greenboi.speed = 200
greenboi.backward(10)
for k in range(500):
    greenboi.backward(k)
    greenboi.right(2)
    greenboi.forward(k)

window.close_on_mouse_click()