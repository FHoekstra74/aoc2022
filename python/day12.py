from collections import deque
f, grid, alla = [line.strip() for line in open("../input/day12.txt", "r")], {}, []
for y, line in enumerate(f):
    for x, c in enumerate(line): 
        grid[(x, y)] = "a" if c == "S" else "z" if c == "E" else c
        if c == "S": start = (x,y)
        if c == "a": alla.append((x,y))
        elif c == "E": end = (x,y)
for run in range(2):
    q, seen = deque(), set()
    for a in [start] if run == 0 else alla + [start]: q.append((a, 0))
    while q:
        pos, dist = q.popleft()
        if pos == end:
            print(dist)
            break
        elif pos in seen: continue
        else:
            seen.add(pos)
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if (pos[0] + dx, pos[1] + dy) in grid and ord(grid[(pos[0] + dx, pos[1] + dy)]) - ord(grid[(pos[0], pos[1])]) <= 1:
                    q.append(((pos[0] + dx, pos[1] + dy), dist + 1))