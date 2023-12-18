import copy

#answer = 105208

#filename = 'sample01.txt'
filename = 'input.txt'

def printgrid(grid):
    print("*"*(len(grid[0])+2))
    for r in grid:
        print("*","".join(r),"*",sep="")
    print("*"*(len(grid[0])+2))

data = []
with open(filename, "r") as f:
    for line in f:
        data.append(list(line.strip()))

visited = {}

rotations = 0
lastround = None
jumped = False
cycles = 1000000000*4
while rotations < cycles:

    maxpercol = [0 for _ in data[0]]

    for ri,row in enumerate(data):
        for ci,chr in enumerate(row):
            if chr == "#":
                maxpercol[ci] = ri+1
            elif chr == "O":
                data[ri][ci] = "."
                data[maxpercol[ci]][ci] = "O"
                maxpercol[ci] += 1

    rotations = rotations + 1
    #if rotations % 4 == 0:
    #    if str(data) == lastround:
    #        print("Found steady state", rotations)
    #        break
    #    else:
    #        lastround = str(data)
    if rotations % 4 == 0 and not jumped:
        if str(data) in visited:
            print("Found one",rotations,visited[str(data)])
            skips = rotations - visited[str(data)]
            print("skips", skips, "jumping ahead", ((cycles-rotations)//skips)*skips)
            rotations = rotations + ((cycles-rotations)//skips)*skips
            jumped = True
        else:
            visited[str(data)] = rotations
            print("Not found",rotations)

    

    #rotate
    data = list(zip(*data[::-1])) # clockwise
    #data = list(zip(*data))[::-1] # counter clockwise
    data = [list(d) for d in data]
    #print("newdata:", data)

    #if rotations % 4 == 0 and jumped:
    #    total = 0
    #    for ri,row in enumerate(data):
    #        for ci,chr in enumerate(row):
    #            if chr == "O":
    #                total += len(data)-ri
    #    print(rotations,total)
    #    printgrid(data)

#data = list(zip(*data[::-1]))
total = 0
for ri,row in enumerate(data):
    for ci,chr in enumerate(row):
        if chr == "O":
            total += len(data)-ri

printgrid(data)
print(total)
