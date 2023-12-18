#answer = 41566
#41472 too low
#41421 too low
#34630

#filename = 'sample01.txt'
filename = 'input.txt'

patterns = []
with open(filename, "r") as f:
    p = []
    for line in f:
        line = line.strip()
        if len(line) > 0:
            p.append(line)
        else:
            patterns.append(p)
            p = []
    patterns.append(p)
#print(patterns)

rowcount = 0
colcount = 0
for p in patterns:
    print("P")
    origrow = None
    origcol = None

    for r in range(len(p)-1):
        mirror = True
        #print("R")
        for i in range(1, 1+min(r+1, len(p)-r-1)):
            if p[r-i+1] != p[r+i]:
                mirror = False
                break
        if mirror:
            print("Orig Mirror r",r+1)
            origrow = r+1
    for c in range(len(p[0])-1):
        mirror = True
        #print("C")
        for i in range(1, 1+min(c+1, len(p[0])-c-1)):
            ca = [row[c-i+1] for row in p]
            cb = [row[c+i] for row in p]
            if ca != cb:
                mirror = False
                break
        if mirror:
            print("Orig Mirror c",c+1)
            origcol = c+1

    foundmirror = False
    for rm in range(len(p)):
        if foundmirror: break
        for cm in range(len(p[0])):
            if foundmirror: break
            pm = [r for r in p]
            pm[rm] = pm[rm][:cm] + ("." if pm[rm][cm] == "#" else "#") + pm[rm][cm+1:]
            print(pm)

            for r in range(len(pm)-1):
                mirror = True
                #print("R")
                span = min(r,len(pm)-r-2)
                if rm in range(r-span,r+span+1):
                    for i in range(1, 1+min(r+1, len(pm)-r-1)):
                        #print("comparing", pm[r-i+1], pm[r+i])
                        if pm[r-i+1] != pm[r+i]:
                            mirror = False
                            break
                    if mirror and r+1 != origrow:
                        print("Mirror r",r+1, (rm,cm), (origrow,origcol))
                        rowcount += r+1
                        foundmirror = True
                        break
                else:
                    mirror = False

            if not foundmirror:
                for c in range(len(pm[0])-1):
                    mirror = True
                    #print("C")
                    span = min(c,len(pm[0])-c-2)
                    if cm in range(c-span,c+span+1):
                        for i in range(1, 1+min(c+1, len(pm[0])-c-1)):
                            ca = [row[c-i+1] for row in pm]
                            cb = [row[c+i] for row in pm]
                            #print("comparing", "".join(ca), "".join(cb))
                            if ca != cb:
                                mirror = False
                                break
                        if mirror and c+1 != origcol:
                            print("Mirror c",c+1, (rm,cm), (origrow,origcol))
                            colcount += c+1
                            foundmirror = True
                            break
                    else:
                        mirror = False
    print("rs=", rowcount, ", cs=", colcount)
        #ca = [c[r-i+1] for c in p]
        #cb = [c[r+i] for c in p]

print(100* rowcount + colcount)
