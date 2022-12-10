f, x, cycle, a, b = [line.strip() for line in open("../input/day10.txt", "r")], 1, 0, 0, [" " * 40] * 6
for line in f:
    for i in range(2 if line.startswith("addx") else 1):
        cycle, row, oldx, x = cycle + 1, (cycle) // len(b[0]), x, x +  (int)(line.split()[1]) if i == 1 else x
        a, b[row] = a + cycle * oldx if cycle in [20, 60, 100, 140, 180, 220] else a, "".join(c if i != cycle - len(b[0]) * row -1 or cycle - len(b[0]) * row -1 not in [oldx - 1, oldx, oldx + 1] else '#' for i, c in enumerate(b[row]))
for line in [a] + b: print(line)
