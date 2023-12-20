#answer = 956

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data.append([int(x) for x in line.strip()])

origin = (0,0)
visited = {}

DIRS = [(-1,0),(0,1),(1,0),(0,-1)] #URDL

best = 9999999999999999999999
found = False

explore = set() #location,direction,direction count,cost
explore.add(((1,0), DIRS[2], 1, data[1][0]))
explore.add(((0,1), DIRS[1], 1, data[0][1]))
while explore:
    loc,dir,dircount,cost = explore.pop()
    key = (loc,dir,dircount)
    if key in visited: #consider also pruning moves that get here with more dir moves left
        prev = visited[key]
        if prev <= cost:
            #prune
            continue
        else:
            visited[key] = cost
    else:
        visited[key] = cost
    if loc == (len(data)-1,len(data[0])-1):
        #at the end
        if cost < best:
            best = cost
            print("Found new best",cost)
    elif cost > best:
        #print("Prune best",cost,best)
        pass #prune, can't beat best
    else:
        for d in [0,3,2,1]: #up,left,down,right
            newloc = (loc[0]+DIRS[d][0], loc[1]+DIRS[d][1])
            newdir = DIRS[d]
            reverse = (-dir[0],-dir[1])
            newcount = 1 + (0 if newdir != dir else dircount)
            if newcount <= 3 and newdir != reverse \
                    and 0 <= newloc[0] < len(data) \
                    and 0 <= newloc[1] < len(data[0]):
                newcost = cost + data[newloc[0]][newloc[1]]
                explore.add((newloc,newdir,newcount,newcost))

print("Best = ",best)