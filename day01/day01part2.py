#answer = 56017

#filename = 'sample02.txt'
filename = 'input.txt'

data = []
total = 0
with open(filename, "r") as f:
    for ind, line in enumerate(f):
        first = None
        last = None
        index = 0
        line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "4").replace("five", "5e").replace("six", "6").replace("seven", "7n").replace("eight", "e8t").replace("nine", "n9e")
        for c in line:
            if c.isdigit():
                if first == None:
                    first = last = c
                else:
                    last = c
                    index = ind

        
        print(first + last)
        total += int(first)*10 + int(last)

print("Total = ", total)
