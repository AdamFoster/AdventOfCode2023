#answer = 31161857

from dataclasses import dataclass, field

#filename = 'sample01.txt'
filename = 'input.txt'

@dataclass
class Interval():
    start: int = field
    length: int = field

@dataclass
class Mapping():
    deststart: int = field
    srcstart: int = field
    length: int = field

data = []
mappings = {}
reversemappings = {}
location = 999999999999
with open(filename, "r") as f:
    seeds = []
    pairs = [int(s) for s in f.readline().strip()[6:].split()]
    while len(pairs)>0:
        start = pairs.pop(0)
        length = pairs.pop(0)
        seeds.append(Interval(start, length))
    #print(seeds)
    
    line = f.readline()
    line = f.readline().strip()
    while line:
        name = line.split()[0]
        src = name.split('-')[0]
        line = f.readline().strip()
        to = name.split('-')[2]
        mappings[src] = {"to": to, "maps": []}
        reversemappings[to] = {"to": src, "maps": []}
        while line and len(line) > 0:
            #deststart, sourcestart, length = [int(s) for s in line.split()]
            mappings[src]["maps"].append([int(s) for s in line.split()])
            reversemappings[to]["maps"].append([int(s) for s in line.split()])
            line = f.readline().strip()
        line = f.readline().strip()


    found = False
    loc = 0
    cursrc = "seed"
    oldintervals = [i for i in seeds]
    #print(oldintervals)
    while cursrc != "location":
        newintervals = []
        while len(oldintervals) > 0:
            iv = oldintervals.pop()
            mapped = False
            for m in mappings[cursrc]["maps"]:
                #print(iv, " : ", m)
                if (m[1] < iv.start and m[1] + m[2]-1 < iv.start) or (m[1] > iv.start+iv.length-1 and m[1] + m[2]-1 > iv.start+iv.length-1):
                    pass # intervals don't overlap
                else:
                    if iv.start < m[1]:
                        oldintervals.append(Interval(iv.start, m[1]-iv.start))
                        iv.length = iv.length - (m[1]-iv.start)
                        iv.start = m[1]
                    if iv.start + iv.length > m[1]+m[2]:
                        oldintervals.append(Interval(m[1]+m[2]+1, iv.start + iv.length - (m[1]+m[2])))
                        iv.length = (m[1]+m[2]) - iv.start
                    
                    newintervals.append(Interval(m[0]+iv.start-m[1], iv.length))
                    mapped = True
                    break
            if not mapped:
                newintervals.append(iv)
        cursrc = mappings[cursrc]["to"]
        oldintervals = newintervals
        #print(newintervals)

    print(sorted([iv.start for iv in oldintervals]))



