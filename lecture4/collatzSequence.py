n = int(input("Enter a positive integer: "))

if (n <= 0):
    exit()

print(n)

while(n != 1):
    if (n % 2 == 0):
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    # print("N type: ", type(n))