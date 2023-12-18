#answer = 27202

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
print(patterns)

rowcount = 0
colcount = 0
for p in patterns:
    print("P")
    for r in range(len(p)-1):
        mirror = True
        print("R")
        for i in range(1, 1+min(r+1, len(p)-r-1)):
            print("comparing", p[r-i+1], p[r+i])
            if p[r-i+1] != p[r+i]:
                mirror = False
                break
        if mirror:
            print("Mirror r",r+1)
            rowcount += r+1

    for c in range(len(p[0])-1):
        mirror = True
        print("C")
        for i in range(1, 1+min(c+1, len(p[0])-c-1)):
            ca = [row[c-i+1] for row in p]
            cb = [row[c+i] for row in p]
            print("comparing", "".join(ca), "".join(cb))
            if ca != cb:
                mirror = False
                break
        if mirror:
            print("Mirror c",c+1)
            colcount += c+1
    print("rs=", rowcount, ", cs=", colcount)
        #ca = [c[r-i+1] for c in p]
        #cb = [c[r+i] for c in p]

print(100* rowcount + colcount)
