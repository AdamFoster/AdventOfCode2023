#answer = 7195

#filename = 'sample01.txt'
filename = 'input.txt'

def countem(springs: str, runs: []): #springs may have ? Convert the first ? into both options and recurse
    #print(springs, type(springs))
    if "?" not in springs:
        #print(springs)
        brokens = filter(None, springs.split("."))
        brokens = [len(b) for b in brokens]
        if brokens == runs:
            return 1
        else:
            return 0
    else:
        q = springs.index("?")
        s1 = springs[:q] + "." + springs[q+1:]
        s2 = springs[:q] + "#" + springs[q+1:]
        return countem(s1, runs) + countem(s2, runs)

data = []
total = 0
with open(filename, "r") as f:
    for line in f:
        #break;
        springs, runs = line.strip().split()
        runs = [int(r) for r in runs.split(",")]

        v = countem(springs, runs)
        print(line, v)
        total += v

print(total)

#print(countem(".??..??...?##.", [1,1,3]))