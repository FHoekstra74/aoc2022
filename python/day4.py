f, a, b = [line.strip().split(",") for line in open("../input/day4.txt", "r")], 0, 0
for i, j, k, l in [((int)(s[0].split("-")[0]), (int)(s[0].split("-")[1]), (int)(s[1].split("-")[0]), (int)(s[1].split("-")[1])) for s in f]:
    a += 1 if (i >= k and j <= l) or (k >= i and l <= j) else 0
    b += 0 if (l < i) or (k > j) else 1
print(a, b)
