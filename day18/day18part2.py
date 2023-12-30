#answer = 36679

filename = 'sample01.txt'
#filename = 'input.txt'


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
data = set()
shadow = {}
curr = (0,0)
shadow[(0,0)] = [(0,0),(1,1)]
with open(filename, "r") as f:
    for line in f:
        dir, dist, color = line.strip().split()
        dist = int(dist)
        color = color[2:-1]
        dir = color[-1]
        if dir == "0": dir = "R"
        elif dir == "1": dir = "D"
        elif dir == "2": dir = "L"
        elif dir == "3": dir = "U"
        else: assert False, "Unknown direction"
        dist = int(color[:-1],base=16)
        instructions.append((dir,dist,color)) 

        curr = (curr[0]+DIRS_L[dir][0], curr[1]+DIRS_L[dir][1])
        data[curr] = color
