#answer = 11024379

#filename = 'sample01.txt'
filename = 'input.txt'

data = [] #0=card id, winning numbers, my numbers, cards won
cards = 0
copies = []
with open(filename, "r") as f:
    for card,line in enumerate(f):
        winners, mine = [set(s.strip().split()) for s in line.split(":")[1].split("|")]
        points = 0
        for w in winners:
            if w in mine:
                points = points + 1
        data.append([card+1, winners, mine, points])
        copies.append(0)
    for i in range(len(data)-1, -1, -1):
        copies[i] = 1
        for j in range(data[i][3]):
            copies[i] = copies[i] + copies[i+j+1]
        print(copies[i])



print(sum(copies))

