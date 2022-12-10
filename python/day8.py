f, trees, a, b = [line.strip() for line in open("../input/day8.txt", "r")], {}, 0, 0
for y, line in enumerate(f):
    for x, c in enumerate(line): trees[(x, y)] = (int)(c)
for i in range(1, x):
    for j in range(1, y):
        thisa, thisb, h = [True] * 4, [0] * 4, trees[(i, j)]
        for num, size, xoff, yoff in [(0, i, -1, 0), (1, j, 0, -1), (2, x - i, 1, 0), (3, y - j, 0, 1)]:
            for k in range(size):
                thisb[num], thisa[num] = thisb[num] + 1 if thisa[num] else thisb[num], False if trees[(i + k * xoff + xoff, j + k * yoff + yoff)] >= h else thisa[num]
        if True in thisa: a += 1
        b = max([b, thisb[0] * thisb[1] * thisb[2] * thisb[3]])
print(a + x * 2 + y * 2, b)
