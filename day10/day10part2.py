#answer = 305

#filename = 'sample02.txt'
filename = 'input.txt'

def printgrid(grid):
    print("*"*(len(grid[0])+2))
    for r in grid:
        print("*","".join(r),"*",sep="")
    print("*"*(len(grid[0])+2))

data = []
start = (0,0) #row,column
with open(filename, "r") as f:
    for row, line in enumerate(f):
        data.append(line.strip())
        if "S" in line:
            start = (row, line.index("S"))

flood = [[" " for _ in data[0]] for _ in data]

dirs = [(-1,0,"|F7"), (0,1,"-J7"), (1,0,"|LJ"), (0,-1,"-LF")]
cur = None
src = None
for d in dirs:
    r,c = start[0]+d[0], start[1]+d[1]
    if 0 <= r < len(data) and 0 <= c < len(data[0]):
        if data[r][c] in d[2]:
            cur = (r,c)
            src = start
            flood[start[0]][start[1]] = data[start[0]][start[1]]
            flood[start[0]+d[1]][start[1]+d[0]] = "A"
            flood[start[0]-d[1]][start[1]-d[0]] = "B"
            break


moves = {}
for d in dirs:
    for c in d[2]:
        if c in moves:
            moves[c] = [moves[c], (-d[0], -d[1])]
        else:
            moves[c] = (-d[0], -d[1])
print(moves)



steps = 1
while cur != start:
    flood[cur[0]][cur[1]] = data[cur[0]][cur[1]]
    #print(cur, data[cur[0]][cur[1]])
    c = data[cur[0]][cur[1]]
    for m in moves[c]:
        if src == (cur[0]+m[0], cur[1]+m[1]): pass
        else:
            src = cur
            cur = (cur[0]+m[0], cur[1]+m[1])
            # dr,dc = src[0]-cur[0], src[1]-cur[1]
            if 0<cur[0]+m[1]<len(flood) and 0<cur[1]-m[0]<len(flood[0]) and flood[cur[0]+m[1]][cur[1]-m[0]] == " ":
                flood[cur[0]+m[1]][cur[1]-m[0]] = "A"
            if 0<cur[0]-m[1]<len(flood) and 0<cur[1]+m[0]<len(flood[0]) and flood[cur[0]-m[1]][cur[1]+m[0]] == " ":
                flood[cur[0]-m[1]][cur[1]+m[0]] = "B"
            if 0<src[0]+m[1]<len(flood) and 0<src[1]-m[0]<len(flood[0]) and flood[src[0]+m[1]][src[1]-m[0]] == " ":
                flood[src[0]+m[1]][src[1]-m[0]] = "A"
            if 0<src[0]-m[1]<len(flood) and 0<src[1]+m[0]<len(flood[0]) and flood[src[0]-m[1]][src[1]+m[0]] == " ":
                flood[src[0]-m[1]][src[1]+m[0]] = "B"
            break
    if steps==20:
        pass
    steps+=1


for r in range(len(flood)): #not a true flood fill... but good enough
    for c in range(len(flood[0])):
        char = flood[r][c]
        if char == "A" or char == "B":
            visited = set()
            visited.add((r,c))
            going = True
            while going:
                going = False
                for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r+d[0], c+d[1]
                    if (nr,nc) in visited:
                        pass
                    else:
                        if 0<=nr<len(flood) and 0<=nc<len(flood[0]) and flood[nr][nc] == " ":
                            flood[nr][nc] = char
                            going = True
                    visited.add((nr,nc))

aes = 0
bes = 0

for r in range(len(flood)):
    for c in range(len(flood[0])):
        if flood[r][c] == "A":
            aes += 1
        elif flood[r][c] == "B":
            bes += 1
#print(start)
printgrid(flood)
print("A=",aes,". B=",bes)



