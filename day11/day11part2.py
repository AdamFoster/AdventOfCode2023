#answer = 411142919886

#filename = 'sample01.txt'
filename = 'input.txt'

expansionratio = 1000000

def printgrid(grid):
    print("*"*(len(grid[0])+2))
    for r in grid:
        print("*","".join(r),"*",sep="")
    print("*"*(len(grid[0])+2))

origgalaxies = set()
expansionrows = []
expansioncolumns = []
data = []
with open(filename, "r") as f:
    for r,line in enumerate(f):
        line = line.strip()
        data.append(line.strip())
        if "#" not in line:
            expansionrows.append(r)
        else:
            for col,chr in enumerate(line):
                if chr == "#":
                    origgalaxies.add((r,col))

for c in range(len(data[0])):
    if "#" not in [d[c] for d in data]:
        expansioncolumns.append(c)

expansionrows.sort()
expansioncolumns.sort()


distance = 0
count = 1
others = set([g for g in origgalaxies])
for g in origgalaxies:
    others.remove(g)
    for t in others:
        if g == t:
            assert False
        else:
            d = abs(g[0]-t[0]) + abs(g[1]-t[1])
            for r in range(min(g[0],t[0]),max(g[0],t[0])):
                if r in expansionrows:
                    d += expansionratio-1
            for c in range(min(g[1],t[1]),max(g[1],t[1])):
                if c in expansioncolumns:
                    d += expansionratio-1
            distance += d
            #print(count, g,t,d)
            count += 1

printgrid(data)
print(origgalaxies)
print(distance)