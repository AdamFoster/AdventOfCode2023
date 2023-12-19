#answer = 286097

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
with open(filename, "r") as f:
    data = f.readline().strip().split(",")

def h(code:str):
    cv = 0
    for c in code:
        cv += ord(c)
        cv = (cv*17) % 256
    return cv

boxes = [[] for _ in range(256)]

for cmd in data:
    boxnum = -1
    if "-" in cmd:
        code = cmd[:-1]
        boxnum = h(code)
        #print(boxnum, cmd, len(boxes))
        for i in range(len(boxes[boxnum])):
            #print(i, boxes[boxnum])
            if boxes[boxnum][i][0] == code:
                boxes[boxnum].pop(i)
                break
    elif "=" in cmd:
        code = cmd[:-2]
        boxnum = h(code)
        num = int(cmd[-1])
        found = False
        #print(boxnum, cmd, len(boxes))
        for i in range(len(boxes[boxnum])):
            if boxes[boxnum][i][0] == code:
                boxes[boxnum][i][1] = num
                found = True
        if not found:
            boxes[boxnum].append([code,num])
    else:
        assert False, "-= not found"
    #print(boxnum, cmd, boxes[boxnum])

total = 0
for i,cmd in enumerate(boxes):
    for j,l in enumerate(cmd):
        score = (i+1) * (j+1) * cmd[j][1]
        print(i,j,score)
        total = total + score
print(total)

#print(h("rn"))