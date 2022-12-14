from collections import defaultdict

def printgrid(grid):
    minx, maxx, miny, maxy = 500, 500, 0, 0
    for k, _ in grid.items():
        minx, miny, maxx, maxy = min([minx, k[0]]), min([miny, k[1]]), max([maxx, k[0]]), max([maxy, k[1]])
    for y in range(miny, maxy + 1):
        line = ""
        for x in range(minx, maxx + 1):
            if (x, y) in grid: 
                line += grid[(x,y)] if len(grid[(x,y)]) > 0 else "."
            else: line += "."
        print(line)

f, grid = [line.strip() for line in open("../input/day14.txt", "r")], defaultdict(str)
for line in f:
    s = line.split(" -> ")
    for k in range(len(s) - 1):
        fromx, fromy = [(int)(i) for i in s[k].split(",")]
        tox, toy = [(int)(i) for i in s[k + 1].split(",")]
        if fromx == tox:
            if toy > fromy:
                for y in range(toy - fromy + 1): grid[ (fromx, fromy + y ) ] = "#"
            else:
                for y in range(fromy - toy + 1): grid[ (fromx, toy + y ) ] = "#"
        if fromy == toy:
            if tox < fromx:
                for x in range(fromx - tox + 1): grid[(tox + x, fromy ) ] = "#"
            else:
                for x in range(tox - fromx + 1): grid[(fromx + x, fromy ) ] = "#"

grid[(500, 0)] = "+"
minx, maxx, miny, maxy = 500, 500, 0, 0
for k, _ in grid.items():
    minx, miny, maxx, maxy = min([minx, k[0]]), min([miny, k[1]]), max([maxx, k[0]]), max([maxy, k[1]])
for x in range(maxx * 2): grid[(x, maxy + 2)] = "#"

orggrid = grid.copy()
for run in range(2):
    res = 0
    if run == 1: grid = orggrid
    while(True):
        posx, posy, ready, res = 500, 0, False, res + 1
        while not ready:
            if grid[(posx, posy + 1)] not in ["o", "#"]:
                posy += 1
            elif grid[(posx - 1, posy + 1)] not in ["o", "#"]:
                posy += 1
                posx -= 1
            elif grid[(posx + 1, posy + 1)] not in ["o", "#"]:
                posy += 1
                posx += 1
            else:
                grid[(posx, posy)] = "o"
                ready = True
                if grid[(500, 0)] in ["o"]: break
            if posy == maxy and run == 0: break
        if not ready and (run == 0) or grid[(500, 0)] in ["o"]: break
    if run == 0: print(res - 1) 
    else: print(res)