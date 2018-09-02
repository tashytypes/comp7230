fh = open("foo.txt", "w")
for i in range(10):
    fh.write(str(i) + "\n")
fh.close()


