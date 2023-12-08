#answer = 57075758

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
mappings = {}
location = 999999999999
with open(filename, "r") as f:
    seeds = [int(s) for s in f.readline().strip()[6:].split()]

    line = f.readline()
    line = f.readline().strip()
    while line:
        name = line.split()[0]
        src = name.split('-')[0]
        line = f.readline().strip()
        mappings[src] = {"to": name.split('-')[2], "maps": []}
        while line and len(line) > 0:
            #sourcestart, deststart, length = [int(s) for s in line.split()]
            mappings[src]["maps"].append([int(s) for s in line.split()])
            line = f.readline().strip()
        line = f.readline().strip()
        mappings["location"] = {"to": "finish"}

    for seed in seeds:
        cursrc = "seed"
        num = seed
        while cursrc != "location":
            for m in mappings[cursrc]["maps"]:
                if m[1] <= num < m[1]+m[2]:
                    #print(m)
                    dest = m[0]+num-m[1]
                    #print("mapped to", mappings[cursrc]["to"], num, "->", dest)
                    num = dest
                    break
            cursrc = mappings[cursrc]["to"]
        if location > num:
            location = num

print("best location", location)

