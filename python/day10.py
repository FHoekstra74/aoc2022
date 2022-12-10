f, x, cycle, a, b = [line.strip() for line in open("../input/day10.txt", "r")], 1, 0, 0, [" " * 40] * 6
for line in f:
    for i in range(2 if line.startswith("addx") else 1):
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]: a += cycle * x
        ln = (cycle - 1) // len(b[0])
        if cycle - (len(b[0]) * ln) -1 in [x - 1, x, x + 1]: b[ln] = "".join(c if i != (cycle - (len(b[0]) * ln) -1) else '#' for i, c in enumerate(b[ln]))
    if line.startswith("addx"): x += (int)(line.split()[1])
print(a)
for line in b: print(line)
