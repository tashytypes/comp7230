#function to compute a square root using the Babylonian Algorithm

def square_root(x):
    y = 0.5 * x
    t = 1
    while (abs(y * y - x) > 1.0e-6):
        y = 0.5 * (y + x/y)
        print("Type of y %s" % type(t))
    return y

print("Square root: %s" % square_root(10))