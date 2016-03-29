import numpy as np
import cube

def main():
    print "Please input red face's squares, with white face on top, going from top left to bottom right (r,o,g,b,y,w,)"
    redface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Please do same with green instead of red"
    greenface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Now Orange"
    orangeface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Blue"
    blueface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Now do white on front and green on top"
    whiteface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Now yellow on front"
    yellowface = raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()

    print "Calculating..."
    print "To solve, hold yellow on top and green on front"

    uh = Cube(redface,greenface,orangeface,blueface,whiteface,yellowface)


main()
