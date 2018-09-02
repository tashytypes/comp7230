# COMP7230 WEEK 1

## Lecture 2: Introduction to Coding

Programming Languages (Referring to Python mainly in this course)
   - A program is a sequence of instructions that a computer will interpret to complete a task
        - Some languages don't execute instructions in sequence -- but this is not the case with python)
   - A program needs to be understood by the computer and by other programmers 
        - Programs are written for people not machines
   - The difference between imperative and declarative knowledge is an important distinction (Python is the former)
        - Declarative Knowledge (using square root as an example) is when we are told "√x = y", "y ** 2 = x", i.e. the square root of x is y, but we are not told how to compute it.
        - Imperative (Procedural) Knowledge is when a recipe / procedure / steps are given to perform a task. 
            1. Initialize - start with a guess - y
            2. Check - if y **2 = approx x, stop
            3. Update 
            4. Repeat - return to step 2

    #Calculates area and circumference #of a circle

    import math

    # radius
    radius = float(input("Enter Radius"))
    # area
    area = math.pi * radius ** 2

    # circumference
    circumference = 2 * math.pi * radius

    print (area, circumference)

A variable is used to store data in a computer program. Variable names are case sensitive and need to be descriptive to aid documentation, can consider using a naming convention like underscores or CamelCase. 

Operator precedence - python will compute prders in a certain order depending on their level or precedence. Parentheses can be used to ensure expressions are evaluated in  the correct order.

Variable assignment is used by the equals sing "=" and the expression needs to be on the right hand side, and just the variable name on the left. This allows for the expression to be evaluated, and for the varialbe to be updated as necessary
      
       count = 1
       count = count + 1
       
Variables can be extensions of a library (module) - e.g. math.pi
    
Program Execution Flow




