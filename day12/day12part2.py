#answer = 

#filename = 'sample01.txt'
filename = 'input.txt'

cache = dict() # (str prefix length, runs prefix length) => combos

def countem2(springs: str, runs: []): #springs may have ? Convert the first ? into both options and recurse, cutting at breaks
    pass


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
        if sum(runs) > len(springs.replace(".","")):
            #print("Prune not enough chars")
            return 0
        brokens = list(filter(None, springs.split(".")))

        # try to prune
        for i,b in enumerate(brokens):
            if i >= len(runs):
                assert i == len(runs)
                return countem(springs.replace("?", "."), runs)
            if "?" in b:
                q = b.index("?")
                if q > runs[i]: #prune if too many broken springs now #index error
                    #print("Prune too many", springs, i)
                    return 0
                if sum(runs[i:])-runs[i]+len(runs)-i-1 > len(springs)-springs.index("?"): #prune if not enough charcters left
                    #print("Prune not spac", springs, i)
                    return 0
                break
            else:
                if runs[i] != len(b):
                    #print("Prune", springs, "at", i)
                    return 0
        #print("Still going on ", springs, runs)

        q = springs.index("?")
        s1 = springs[:q] + "." + springs[q+1:]
        s2 = springs[:q] + "#" + springs[q+1:]

        s1brokens = list(filter(None, springs[:q].split(".")))

        c1 = -1
        # check cache
        for i, b in enumerate(s1brokens):
            if i >= len(runs):
                assert i == len(runs)
                break
            if runs[i] != len(b):
                if (q,i-1) in cache:
                    #print("Cache hit: ", springs, (q,i-1), cache[(q,i-1)])
                    c1 = cache[(q,i-1)]
                    break
                
        if c1 == -1:                
            c1 = countem(s1, runs)
            for i, b in enumerate(s1brokens):
                if runs[i] != len(b):
                    cache[(q,i-1)] = c1
                    #print("Cache add: ", springs, (q,i-1), cache[(q,i-1)])
                    break
        totalcount = c1 + countem(s2, runs)

        return totalcount

data = []
total = 0
with open(filename, "r") as f:
    for line in f:
        #break;
        springs, runs = line.strip().split()
        springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
        runs = [int(r) for r in runs.split(",")]
        runs = runs + runs + runs + runs + runs
        #print(runs, springs)
        #break
        v = countem(springs, runs)
        print(line.strip(), "=", v)
        total += v
        

print(total)

#print(countem("???.###????.###????.###????.###????.###", [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3]))
#print(countem(".??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.", [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3]))
#print(countem("?###??????????###??????????###??????????###??????????###????????", [3,2,1,3,2,1,3,2,1,3,2,1,3,2,1]))