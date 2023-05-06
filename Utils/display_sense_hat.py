#Display the scrolling message
def displayMessage(colours, senseHat):
    tup_colours = eval(colours)
    senseHat.show_message("Data sent it !", scroll_speed=0.05, back_colour=tup_colours)
    senseHat.clear()