### python by moshiurr007 --> beginner_level ###

# hollow rectangle #

def rectangle(width, height):
    if not 5 <= width <= 50 or not 4 <= height <= 40:
        return "Try with width 5 to 50 and height 4 to 40 for a better visual result."

    result = ""

    for i in range(1, height+1):
        if i == 1: # first line
            result += "* " * width + "\n"  # added space after each *
        elif i == height: # last line
            result += "* " * width  # added space after each *

        else: # any of the middle lines
            result += "*" + " "*(2*width-3) + "*\n"

    return result

print(rectangle(5,4))

""" Output:
* * * * * 
*       *
*       *
* * * * * 
"""