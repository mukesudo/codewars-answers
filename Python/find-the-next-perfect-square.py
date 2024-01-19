from math import sqrt


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    squareroot = sqrt(sq)
    if squareroot-int(squareroot)==0:
        return pow((int(squareroot)+1),2)
    else:
         return -1