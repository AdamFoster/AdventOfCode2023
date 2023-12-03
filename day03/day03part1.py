#answer = 550064

#filename = 'sample01.txt'
filename = 'input.txt'

data = []
h = 0
w = 0
total = 0
with open(filename, "r") as f:
    for line in f:
        data.append(line.strip())
    h = len(data)
    w = len(data[0])

    for row, line in enumerate(data):
        i = 0
        while i < w:
            if i<w and line[i].isdigit():
                num = int(line[i])
                start = i
                end = i
                i = i+1
                while i<w and line[i].isdigit():
                    num = 10*num + int(line[i])
                    end = i
                    i = i+1
                print(num)

                valid = False
                if row > 0:
                    if start > 0:
                        if not (data[row-1][start-1].isdigit() or data[row-1][start-1] == "."):
                            valid = True
                    if end < w-1:
                        if not (data[row-1][end+1].isdigit() or data[row-1][end+1] == "."):
                            valid = True
                    for c in data[row-1][start:end+1]:
                        if not (c.isdigit() or c == "."):
                            valid = True

                if row < h-1:
                    if start > 0:
                        if not (data[row+1][start-1].isdigit() or data[row+1][start-1] == "."):
                            valid = True
                    if end < w-1:
                        if not (data[row+1][end+1].isdigit() or data[row+1][end+1] == "."):
                            valid = True
                    for c in data[row+1][start:end+1]:
                        if not (c.isdigit() or c == "."):
                            valid = True

                if start > 0:
                    if not (data[row][start-1].isdigit() or data[row][start-1] == "."):
                        valid = True
                if end < w-1:
                        if not (data[row][end+1].isdigit() or data[row][end+1] == "."):
                            valid = True

                if valid:
                    total = total + num
            else:
                i = i+1
print(data)
print(total)
