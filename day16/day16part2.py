#answer = 7488

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    for line in f:
        data.append(line.strip())


def printvisited(visited):
    lit = set([v[0] for v in visited])
    for i,row in enumerate(data):
        for j,chr in enumerate(row):
            if (i,j) in lit:
                print("#", end="")
            else:
                print(".", end="")
        print()

dirs = [(-1,0),(0,1),(1,0),(0,-1)] #URDL

def runbeam(origin): #((0,0),dirs[1])) #origin, going right
    beams = []
    visited = set()
    beams.append(origin)
    visited.add(beams[0])
    while len(beams) > 0:
        #print(beams)
        beam = beams.pop()
        if beam[0][0] < 0 or beam[0][0] >= len(data) \
                or beam[0][1] < 0 or beam[0][1] >= len(data[0]):
            #print("Outside grid")
            visited.remove(beam)
            continue #cull cells outside range
        rc = beam[0]
        dir = beam[1]
        if data[rc[0]][rc[1]] == "." \
                or (data[rc[0]][rc[1]] == "-" and dir[0] == 0) \
                or (data[rc[0]][rc[1]] == "|" and dir[1] == 0):
            newbeam = ((rc[0]+dir[0],rc[1]+dir[1]),dir)
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
        elif data[rc[0]][rc[1]] == "-" and dir[1] == 0:
            newbeam = ((rc[0],rc[1]+1),dirs[1])
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
            newbeam = ((rc[0],rc[1]-1),dirs[3])
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
        elif data[rc[0]][rc[1]] == "|" and dir[0] == 0:
            newbeam = ((rc[0]+1,rc[1]),dirs[2])
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
            newbeam = ((rc[0]-1,rc[1]),dirs[0])
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
        elif data[rc[0]][rc[1]] == "\\":
            newbeam = None
            if dir == dirs[0]:
                newbeam = ((rc[0],rc[1]-1),dirs[3])
            elif dir == dirs[1]:
                newbeam = ((rc[0]+1,rc[1]),dirs[2])
            elif dir == dirs[2]:
                newbeam = ((rc[0],rc[1]+1),dirs[1])
            elif dir == dirs[3]:
                newbeam = ((rc[0]-1,rc[1]),dirs[0])
            else:
                assert False, "\\"
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
        elif data[rc[0]][rc[1]] == "/":
            newbeam = None
            if dir == dirs[0]:
                newbeam = ((rc[0],rc[1]+1),dirs[1])
            elif dir == dirs[1]:
                newbeam = ((rc[0]-1,rc[1]),dirs[0])
            elif dir == dirs[2]:
                newbeam = ((rc[0],rc[1]-1),dirs[3])
            elif dir == dirs[3]:
                newbeam = ((rc[0]+1,rc[1]),dirs[2])
            else:
                assert False, "\\"
            if newbeam in visited:
                pass
            else:
                visited.add(newbeam)
                beams.append(newbeam)
        else:
            print(beam, data[rc[0]][rc[1]])
            assert False, beam
            
    lit = set([v[0] for v in visited])
    #print(lit)
    #print(len(lit))
    return len(lit)
#printvisited(visited)

maxlit = 0
for ri in range(len(data)):
    litcount = runbeam(((ri,0),dirs[1]))
    if litcount > maxlit:
        maxlit = litcount
    litcount = runbeam(((ri,len(data[0])-1),dirs[3]))
    if litcount > maxlit:
        maxlit = litcount
for ci in range(len(data[0])):
    litcount = runbeam(((0,ci),dirs[2]))
    if litcount > maxlit:
        maxlit = litcount
    litcount = runbeam(((len(data)-1,ci),dirs[0]))
    if litcount > maxlit:
        maxlit = litcount

print(maxlit)