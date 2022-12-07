f, cur, sizes = [line.strip() for line in open("../input/day7.txt", "r")], "", {}
for cmd in [line.split() for line in f]:
    if cmd[1] == "cd":
        if cmd[2] == "..": cur = " ".join(cur.split()[:-1])
        else: cur = cur + " " + cmd[2] if len(cur) > 0 else cmd[2]
        if cur not in sizes: sizes[cur] = 0
    elif cmd[0].isnumeric():
        dir = ""
        for j in cur.split():
            dir += " " + j if len(dir) > 0 else j
            sizes[dir] += int(cmd[0])
print(sum([s for s in sizes.values() if s <= 100000]))
print(min([s for s in sizes.values() if s > (30000000 - (70000000 - sizes["/"]))]))