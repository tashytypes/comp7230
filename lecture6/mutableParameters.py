def f(x):
    """"Returns the sum of the elements in a list""" #while loop

    sx = 0
    while(len(x) > 0):
        sx += x.pop()
    return sx

def g(x):
    """"Returns the sum of the elements in a list""" #for loop

    sx = 0
    for i in x:
        sx += i
    return sx

grades = [20, 75, 85, 77]
print(grades)

h = f(grades)
s = g(grades)

print(h)
print(s)
