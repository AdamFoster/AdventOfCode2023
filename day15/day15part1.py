#answer = 517551

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    data = f.readline().strip().split(",")

total = 0
for d in data:
    cv = 0
    for c in d:
        cv += ord(c)
        cv = (cv*17) % 256
    total += cv

print(total)
