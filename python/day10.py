def handlecycle(cycle,x,a,b):
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]: a += cycle * x
    line = (cycle - 1) // len(b[0])
    if cycle - (len(b[0]) * line) -1 in [x - 1, x, x + 1]:
        l = list(b[line])
        l[cycle - (len(b[0]) * line) -1] = "#"
        b[line] = "".join(l)
    return cycle, a, b

f, x, cycle, a, b = [line.strip() for line in open("../input/day10.txt", "r")], 1, 0, 0, [" " * 40] * 6
for line in f:
    cycle, a, b = handlecycle(cycle, x, a, b)
    if line.startswith("addx"):
        cycle, a, b = handlecycle(cycle, x, a, b)
        x += (int)(line.split()[1])
print(a)
for line in b: print(line)