"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Steven Kay.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(100)
########################################################################
#
# Done: 2.
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#
#    - Constructs a SimpleTurtle with a  'blue'  Pen.
#
blueboi = rg.SimpleTurtle('square')
blueboi.pen = rg.Pen('blue', 3)
point2 = rg.Point(0, 0)
blueboi.go_to(point2)
#    - Makes the SimpleTurtle go straight UP 200 pixels.
#
blueboi.left(90)
blueboi.forward(200)
#    - Makes the SimpleTurtle lift its pen UP
#         (so that the next movements do NOT leave a "trail")
#         HINT: Use the "dot trick" to figure out how to do this.
#
blueboi.pen_up()
#    - Makes the SimpleTurtle go to the Point at (100, -40).
##
point1 = rg.Point(100, -40)

blueboi.go_to(point1)
blueboi.pen_down()

blueboi.forward(150)
#   Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#   As always, test by running the module.
#   As always, COMMIT-and-PUSH when you are done with this module.
#
########################################################################
window.close_on_mouse_click()