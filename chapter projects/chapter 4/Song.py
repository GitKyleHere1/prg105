# A program to sing to you the song '99 bottles of beer on the wall' with correct grammar

# Initiate variables
bottles = 99
bottle_type = "bottles"

# Initiate the loop and start the song
while bottles != 0:
    print("%d %s of beer on the wall," % (bottles, bottle_type))
    print("%d %s of beer." % (bottles, bottle_type))
    print("Take one down, pass it around,")

    # Remove 1 bottle from the wall
    bottles -= 1

    # If we have 1 bottle left, then we don't want to say 'bottles' anymore
    if bottles == 1:
        bottle_type = "bottle"
    # And if we have 0 bottles left, we don't want to say 'bottle'
    elif bottles == 0:
        bottle_type = "bottles"

    print("%d %s of beer on the wall.\n" % (bottles, bottle_type))
