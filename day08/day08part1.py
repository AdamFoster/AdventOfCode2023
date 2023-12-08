#answer = 13939

#filename = 'sample02.txt'
filename = 'input.txt'

data = {}
with open(filename, "r") as f:
    steps = [0 if a == "L" else 1 for a in f.readline().strip()]
    #print(steps)
    f.readline()
    line = f.readline()
    while line:
        start, rest = line.split("=")
        rest = rest.strip()[1:-1]
        jumps = [r.strip() for r in rest.split(",")]
        #print(jumps)
        line = f.readline()
        data[start.strip()] = jumps
    #print(data)
    
    cur = "AAA"
    step = 0
    count = 0
    while cur != "ZZZ":
        cur = data[cur][steps[step]]
        step = (step+1)%len(steps)
        count = count + 1
    print(count)

