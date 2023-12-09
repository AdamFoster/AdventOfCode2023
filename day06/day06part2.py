#answer = 33149631

#filename = 'sample01.txt'
filename = 'input.txt'

with open(filename, "r") as f:
    t = int("".join(f.readline().strip().split()[1:]))
    r = int("".join(f.readline().strip().split()[1:]))
    print(t,r)

    #d = t*h - h^2
    #t*h - h^2 > r
    #0 > h^2 - t*h + r
    #h = t +- sqrt(t*t - 4*r) / 2
    disc = (t*t - 4*r) ** 0.5
    x0 = (t - disc) / 2
    x1 = (t + disc) / 2
    print(x0)
    print(x1)
    print(x1-x0)

    #total = 1
    #for t,r in zip(times, records):
    #    winners = 0
    #    for held in range(t):
    #        d = (t-held)*held

    #        if d > r:
    #            winners += 1
    #    if winners > 0:
    #        total = total * winners
    #    print(winners)
    #print("Total:", total)
