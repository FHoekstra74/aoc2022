from collections import deque
f, a, b, cubes, trapped = [line.strip() for line in open("../input/day18.txt", "r")], 0, 0, set(), set()
for line in f: cubes.add(tuple(int(i) for i in line.split(",")))
maxc, minc = (max([max(x, y, z) for x, y, z in cubes])), (min([min(x, y, z) for x, y, z in cubes]))
for x in range(maxc + 1):
    for y in range(maxc + 1):
        for z in range(maxc + 1):
            testcube = (x, y, z)
            if testcube not in cubes:           
                q, seen, open = deque(), set(), False
                q.append(testcube)
                seen.add(testcube)
                while q and not open:
                    x1, y1, z1 = q.popleft()
                    if min(x1, y1, z1) < minc or max(x1, y1, z1) >  maxc: open = True
                    else:        
                        for neighbour in [(x1 + 1, y1, z1), (x1 - 1, y1, z1), (x1, y1 + 1, z1), (x1, y1 - 1, z1), (x1, y1, z1 + 1), (x1, y1, z1 - 1)]:
                            if neighbour not in seen and neighbour not in cubes:
                                seen.add(neighbour)
                                q.append(neighbour)
                if not open: trapped.add(testcube)
for x, y, z in cubes:
    for neighbour in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]:
        if neighbour not in cubes: a += 1
        if neighbour not in cubes and neighbour not in trapped: b += 1
print(a, b)
