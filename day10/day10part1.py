#answer = 6831

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
start = (0,0) #row,column
with open(filename, "r") as f:
    for row, line in enumerate(f):
        data.append(line.strip())
        if "S" in line:
            start = (row, line.index("S"))

dirs = [(-1,0,"|F7"), (0,1,"-J7"), (1,0,"|LJ"), (0,-1,"-LF")]
cur = None
src = None
for d in dirs:
    r,c = start[0]+d[0], start[1]+d[1]
    if 0 <= r < len(data) and 0 <= c < len(data[0]):
        if data[r][c] in d[2]:
            cur = (r,c)
            src = start
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
    print(cur, data[cur[0]][cur[1]])
    c = data[cur[0]][cur[1]]
    for m in moves[c]:
        if src == (cur[0]+m[0], cur[1]+m[1]): pass
        else:
            src = cur
            cur = (cur[0]+m[0], cur[1]+m[1])
            break
    if steps==20:
        pass
    steps+=1


#print(start)
print(steps//2)



