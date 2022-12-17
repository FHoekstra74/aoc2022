rocks = [((0,0),(1,0),(2,0),(3,0)), ((1,0),(0,1),(1,1),(2,1),(1,2)), ((0,0),(1,0),(2,0),(2,1),(2,2)), ((0,0),(0,1),(0,2),(0,3)), ((0,0),(1,0),(0,1),(1,1))]
gas = [line.strip() for line in open("../input/day17.txt", "r")][0]
moves = {'<': (-1, 0), '>': (1, 6)}
grid, maxy, nextrock, gaspos, codes, i = set(), 0, 0, 0, {}, 0

while i < 1000000000000:
    newrock = set()
    for (rx, ry) in rocks[nextrock]: newrock.add((2 + rx, maxy + 3 + ry))
    nextrock = 0 if nextrock == 4 else nextrock + 1
    move = True
    while move:
        direction, border = moves[gas[gaspos]]
        gaspos = 0 if gaspos == len(gas) - 1 else gaspos + 1
        canmove = True
        for point in newrock:
            if point[0] == border or (point[0] + direction, point[1]) in grid: 
                canmove = False
                break
        if canmove:
            newrock2 = set()
            for point in newrock: newrock2.add((point[0] + direction, point[1]))
            newrock = newrock2
        canmove = True
        for point in newrock:
            if point[1] == 0 or (point[0], point[1] -1) in grid: 
                canmove = False
                break
        if canmove:
            newrock2 = set()
            for point in newrock: newrock2.add((point[0],point[1]-1))
            newrock = newrock2
        else:
            move = False
    for point in newrock: grid.add(point)
    maxy = max([y for x,y in grid]) + 1
    newgrid = set()
    for point in grid:
        if point[1] > maxy - 50:
            newgrid.add(point)
    grid = newgrid
    if i == 2022: print("a:", maxy)
    i += 1
    if i > 2000 and i < 100000:
        code = ""
        for j in range(40):
            for x in range(7):
                if (x, maxy - j) in grid: code += (str)(x)
        if code not in codes: codes[code] = (i, maxy)
        else:
            dy, di = maxy - codes[code][1], i - codes[code][0] 
           # print("in", di, "stappen gaat y", dy, "omhoog")
            steps = (1000000000000 -i -di) // di
            i, maxy = i + steps * di, maxy + steps * dy
            newgrid = set()
            for point in grid: newgrid.add((point[0],point[1] + steps * dy))
            grid = newgrid
print("b:", maxy)
