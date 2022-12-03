f, a, b = [line.strip() for line in open("../input/day3.txt", "r")], 0, 0
for index, item in enumerate([(l, l[len(l) // 2 :]) for l in f]):
    c = [c for c in item[0] if c in item[1]][0]
    a += ord(c) - 96 if c.islower() else ord(c) - 38
    if (index + 1) % 3 == 0:
        c = [c for c in f[index-2] if c in f[index-1] and c in item[0]][0]
        b += ord(c) - 96 if c.islower() else ord(c) - 38
print(a, b)