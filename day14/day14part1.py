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

maxpercol = [0 for _ in data[0]]

for ri,row in enumerate(data):
    for ci,chr in enumerate(row):
        if chr == "#":
            maxpercol[ci] = ri+1
        elif chr == "O":
            data[ri][ci] = "."
            data[maxpercol[ci]][ci] = "O"
            maxpercol[ci] += 1

total = 0
for ri,row in enumerate(data):
    for ci,chr in enumerate(row):
        if chr == "O":
            total += len(data)-ri

printgrid(data)
print(total)
