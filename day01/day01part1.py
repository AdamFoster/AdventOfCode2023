#answer = 56506

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
total = 0
with open(filename, "r") as f:
    for line in f:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first == None:
                    first = last = c
                else:
                    last = c
        print(first + last)
        total += int(first)*10 + int(last)

print("Total = ", total)
