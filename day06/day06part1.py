#answer = 2449062

#filename = 'sample01.txt'
filename = 'input.txt'

with open(filename, "r") as f:
    times = [int(x) for x in f.readline().strip().split()[1:]]
    records = [int(x) for x in f.readline().strip().split()[1:]]

    total = 1
    for t,r in zip(times, records):
        winners = 0
        for held in range(t):
            d = (t-held)*held
            if d > r:
                winners += 1
        if winners > 0:
            total = total * winners
        print(winners)
    print("Total:", total)
