#answer = 1708206096

from collections import Counter

#filename = 'sample01.txt'
filename = 'input.txt'

total = 0

with open(filename, "r") as f:
    for line in f:
        numbers = [int(x) for x in line.strip().split()]
        working = [x for x in numbers]
        counts = Counter(working)
        pyramid = []
        pyramid.append(working)
        while len(counts) > 1 or working[0] != 0:
            newworking = [a-b for a,b in zip(working[1:], working[0:-1])]
            #print(newworking)
            working = newworking
            counts = Counter(working)
            pyramid.append(working)
            print("working create = ", working)
        pyramid.pop()
        working.append(0)
        while len(pyramid) > 0:
            print("working = ", working)
            row = pyramid.pop()
            working = row + [working[-1] + row[-1]]
            print(working)
        total += working[-1]
            
print(total)