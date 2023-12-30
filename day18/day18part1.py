#answer = 36679

#filename = 'sample01.txt'
filename = 'input.txt'


DIRS = [(-1,0),(0,1),(1,0),(0,-1)] #URDL
DIRS_L = {"U":(-1,0),"R":(0,1),"D":(1,0),"L":(0,-1)}

def printgrid(grid:{}):
    miny = min([k[0] for k in grid.keys()])
    maxy = max([k[0] for k in grid.keys()])
    minx = min([k[1] for k in grid.keys()])
    maxx = max([k[1] for k in grid.keys()])
    print(miny,maxy,minx,maxx)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (y,x) in grid:
                print("#", end='')
            else:
                print(".", end='')
        print()

instructions = []
data = {}
curr = (0,0)
with open(filename, "r") as f:
    for line in f:
        dir, dist, color = line.strip().split()
        dist = int(dist)
        color = color[2:-1]
        instructions.append((dir,dist,color)) 

        for i in range(dist):
            curr = (curr[0]+DIRS_L[dir][0], curr[1]+DIRS_L[dir][1])
            data[curr] = color

printgrid(data)


def floodit(grid:{}):
    flood = set()
    
    miny = min([k[0] for k in grid.keys()])
    maxy = max([k[0] for k in grid.keys()])
    minx = min([k[1] for k in grid.keys()])
    maxx = max([k[1] for k in grid.keys()])
    miny=miny-1
    maxy=maxy+1
    minx=minx-1
    maxx=maxx+1

    floodcheck = set()
    flood.add((miny,minx))
    floodcheck.add((miny,minx))

    while floodcheck:
        f = floodcheck.pop()
        for d in DIRS:
            nf = (f[0] + d[0], f[1]+d[1])
            if nf in flood or nf in floodcheck or nf in data:
                pass
            elif miny<=nf[0]<=maxy and minx<=nf[1]<=maxx:
                flood.add(nf)
                floodcheck.add(nf)

    dy = maxy-miny+1
    dx = maxx-minx+1
    area = dy*dx
    remainder = area - len(flood)
    print("Rest",remainder)
    
    return flood


flood = floodit(data)
#printgrid({f:1 for f in flood})