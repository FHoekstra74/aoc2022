f, trees, a, b = [line.strip() for line in open("../input/day8.txt", "r")], {}, 0, 0
for y, line in enumerate(f):
    for x, c in enumerate(line):
        trees[(x, y)] = c
for i in range(x + 1):
    for j in range(y + 1):
        if i == 0 or j == 0 or i == x or j == y: a += 1
        else:
            a1, a2, a3, a4 = True, True, True, True
            for k in range(i):
                if trees[(k, j)] >= trees[(i, j)]: a1 = False
            for k in range(j):
                if trees[(i, k)] >= trees[(i, j)]: a2 = False
            for k in range(x - i):
                if trees[(i + k + 1, j)] >= trees[(i, j)]: a3 = False
            for k in range(y - j): 
                if trees[(i, j + k + 1)] >= trees[(i, j)]: a4 = False
            if a1 or a2 or a3 or a4: a+=1
            b1, b2, b3, b4 = 0, 0, 0, 0
            for k in range(i):
                b1 += 1
                if trees[(i - k - 1, j)] >= trees[(i, j)]: break
            for k in range(j):
                b2 += 1
                if trees[(i, j - k - 1)] >= trees[(i, j)]: break
            for k in range(x - i):
                b3 += 1
                if trees[(i + k + 1, j)] >= trees[(i, j)]: break
            for k in range(y - j):
                b4 += 1
                if trees[(i, j + k + 1)] >= trees[(i, j)]: break
            if b1 * b2 * b3 * b4 > b: b = b1 * b2 * b3 * b4
print(a)
print(b)
