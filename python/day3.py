f, a, b, first, second = [line.strip() for line in open("../input/day3.txt", "r")], 0, 0, "", ""
for line, secondhalf in [(l, l[len(l) // 2 :]) for l in f]:
    c = [c for c in line if c in secondhalf][0]
    a += ord(c) - 96 if c.islower() else ord(c) - 38
    if len(first) == 0: first = line
    elif len(second) == 0: second = line
    else:
        c = [c for c in first if c in second and c in line][0]
        b += ord(c) - 96 if c.islower() else ord(c) - 38
        first, second = "", ""
print(a, b)