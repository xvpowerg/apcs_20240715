f = open("abc.txt")
line = f.readline()

while line:
    print(line,end="")
    line = f.readline()

