#answer = 9742154

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
        line = line.strip()
        data.append(line.strip())
        if "#" not in line:
            data.append(line)

columnstoadd = []
for c in range(len(data[0])):
    if "#" not in [d[c] for d in data]:
        columnstoadd.append(c)

while columnstoadd:
    c = columnstoadd.pop()
    for r in range(len(data)):
        data[r] = data[r][:c] + "." + data[r][c:]

### Grid is now set up

galaxies = set()
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == "#":
            galaxies.add((r,c))

distance = 0
count = 1
others = set([g for g in galaxies])
for g in galaxies:
    #mindist = 999999999
    others.remove(g)
    for t in others:
        if g == t:
            assert False
        else:
            d = abs(g[0]-t[0]) + abs(g[1]-t[1])
            distance += d
            #print(count, g,t,d)
            count += 1
            #if d < mindist:
            #    mindist = d
    #print(mindist)
    #distance += mindist


printgrid(data)
print(galaxies)
print(distance)