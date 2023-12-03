#answer = 85010461

#filename = 'sample02.txt'
filename = 'input.txt'

data = []
h = 0
w = 0
total = 0

dirs = [[-1,-1], [-1, 0], [-1, 1], [0,-1], [0, 1], [1,-1], [1, 0], [1, 1]]

def getnumber(r, c):
    if not data[r][c].isdigit():
        return None
    while c > 0 and data[r][c-1].isdigit():
        c = c - 1
    n = 0
    start = c
    while c < len(data[r]) and data[r][c].isdigit():
        n = 10*n + int(data[r][c])
        c = c + 1
    return (r, start, n)


with open(filename, "r") as f:
    for line in f:
        data.append(line.strip())
    h = len(data)
    w = len(data[0])

    for row, line in enumerate(data):
        for column, c in enumerate(line):
            if c == "*":
                nums = set()
                for d in dirs:
                    #print("d", d, "for", row, column)
                    if 0 <= row + d[0] < h and 0 <= column + d[1] < w:
                        #print("getnumber(, )", row + d[0], column + d[1])
                        num = getnumber(row + d[0], column + d[1])
                        if num:
                            nums.add(num)
                print(nums, len(nums))
                if len(nums) == 2:
                    total += nums.pop()[2] * nums.pop()[2]

print(data)
print(total)
