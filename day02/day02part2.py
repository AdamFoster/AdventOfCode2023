#answer = 71585

#filename = 'sample01.txt'
filename = 'input.txt'

total = 0

with open(filename, "r") as f:
    for line in f:
        game, rest = line.split(":")
        game = int(game[5:])
        colours = {"red": 0, "green": 0, "blue": 0}
        for round in rest.split(";"):
            draws = round.strip().split(',')
            for draw in draws:
                count, colour = draw.strip().split()
                if int(count) > colours[colour]:
                    colours[colour] = int(count)
        total += colours["red"]*colours["green"]*colours["blue"]
print(total)

