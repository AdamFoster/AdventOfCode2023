#answer = 21485

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
total = 0
with open(filename, "r") as f:
    for line in f:
        winners, mine = [set(s.strip().split()) for s in line.split(":")[1].split("|")]
        points = 0
        print(winners, mine)
        for w in winners:
            if w in mine:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
        print(points)
        total = total + points

print(total)

