def printgird(grid):
    ymax=0
    for point in grid:
        ymax = max(point[1], ymax)
    for y in range(ymax, 0 - 1, -1):
        line = "|"
        for x in range(0, 7):
            if (x, y) in grid: line += "#"
            else: line += "."
        line += "|"
        print(line)

rocks = [((0,0),(1,0),(2,0),(3,0)), ((1,0),(0,1),(1,1),(2,1),(1,2)), ((0,0),(1,0),(2,0),(2,1),(2,2)), ((0,0),(0,1),(0,2),(0,3)), ((0,0),(1,0),(0,1),(1,1))]
#gas = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
gas = [line.strip() for line in open("../input/day17.txt", "r")][0]
moves = {'<': (-1, 0), '>': (1, 6)}
grid, maxy, nextrock, gaspos = set(), 0, 0, 0

for i in range(2022):
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

printgird(grid)
print(maxy)
