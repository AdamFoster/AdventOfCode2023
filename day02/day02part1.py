#answer = 2331

#filename = 'sample01.txt'
filename = 'input.txt'

total = 0
maxset = {"red": 12, "green": 13, "blue": 14}
with open(filename, "r") as f:
    for line in f:
        game, rest = line.split(":")
        game = int(game[5:])
        for round in rest.split(";"):
            draws = round.strip().split(',')
            for draw in draws:
                count, colour = draw.strip().split()
                if int(count) > maxset[colour]:
                    print("Illegal: ", line)
                    game = 0
        total = total + game
print(total)

