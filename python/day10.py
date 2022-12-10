f, x, cycle, a, b = [line.strip() for line in open("../input/day10.txt", "r")], 1, 0, 0, [" " * 40] * 6
for line in f:
    for i in range(2 if line.startswith("addx") else 1):
        cycle, crtline = cycle + 1, (cycle) // len(b[0])
        if cycle in [20, 60, 100, 140, 180, 220]: a += cycle * x
        if cycle - len(b[0] * crtline) -1 in [x - 1, x, x + 1]: b[crtline] = "".join(c if i != (cycle - len(b[0] * crtline) -1) else '#' for i, c in enumerate(b[crtline]))
        if i == 1: x += (int)(line.split()[1])
for line in [a] + b: print(line)
