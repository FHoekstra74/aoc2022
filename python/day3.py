f, a, b, first, second = [line.strip() for line in open("../input/day3.txt", "r")], 0, 0, "", ""
for line, secondhalf in [(l, l[len(l) // 2 :]) for l in f]:
    for c in line:
        if c in secondhalf:
            a += ord(c) - 96 if c.islower() else ord(c) - 38
            break
    if len(first) == 0: first = line
    elif len(second) == 0: second = line
    else:
        for c in first:
            if c in second and c in line:
                b += ord(c) - 96 if c.islower() else ord(c) - 38
                break
        first, second = "", ""
print(a, b)