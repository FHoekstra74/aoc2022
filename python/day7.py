f, cur, sizes = [line.strip() for line in open("../input/day7.txt", "r")], "", {}
for cmd in [line.split() for line in f]:
    if cmd[1] == "cd":
        if cmd[2] == "..": cur = " ".join(cur.split()[:-1])
        else:
            cur = cur + " " + cmd[2] if len(cur) > 0 else cmd[2]
            sizes[cur] = 0
    elif cmd[0].isnumeric():
        for i in range(len(cur.split())): sizes[" ".join(cur.split()[:i + 1])] += int(cmd[0])
print(sum([s for s in sizes.values() if s < 100000]))
print(min([s for s in sizes.values() if s > (30000000 - (70000000 - sizes["/"]))]))