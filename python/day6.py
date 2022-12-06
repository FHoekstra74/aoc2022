f, a, b = [line for line in open("../input/day6.txt", "r")], 0, 0
for i in range(len(f[0])):
    if i > 2 and a == 0:
        last = []
        for j in range(4): last.append(f[0][i - j])
        if len(set(last)) == 4: a = i + 1
    if i > 12 and b == 0:
        last = []
        for j in range(14): last.append(f[0][i - j])
        if len(set(last)) == 14: b = i + 1
print(a, b)
