rocks = [((0,0),(1,0),(2,0),(3,0)), ((1,0),(0,1),(1,1),(2,1),(1,2)), ((0,0),(1,0),(2,0),(2,1),(2,2)), ((0,0),(0,1),(0,2),(0,3)), ((0,0),(1,0),(0,1),(1,1))]
gas, moves, grid, maxy, nextrock, gaspos, codes, i = [line.strip() for line in open("../input/day17.txt", "r")][0], {'<': (-1, 0), '>': (1, 6)}, set(), 0, 0, 0, {}, 0

while i < 1000000000000:
    newrock, move = set(), True
    for (rx, ry) in rocks[nextrock]: newrock.add((2 + rx, maxy + 3 + ry))
    nextrock = 0 if nextrock == 4 else nextrock + 1
    while move:
        direction, border = moves[gas[gaspos]]
        gaspos = 0 if gaspos == len(gas) - 1 else gaspos + 1
        if len([x for x, y in newrock if (x + direction, y) in grid or x == border]) == 0: newrock = set([(x + direction, y) for x, y in newrock])
        if len([x for x, y in newrock if (x, y - 1) in grid or y == 0]) == 0: newrock = set([(x, y - 1) for x, y in newrock])
        else: move = False
    for point in newrock: grid.add(point)
    maxy, grid = max([y for x,y in grid]) + 1, set([(x,y) for x,y in grid if y > maxy - 50])
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
            steps = (1000000000000 -i -di) // di
            i, maxy, grid = i + steps * di, maxy + steps * dy, set([(x, y + steps * dy) for x, y in grid])
print("b:", maxy)
