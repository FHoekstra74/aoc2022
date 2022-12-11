f, monkeysa, monkeysb, modulus, mnum = [line.strip() for line in open("../input/day11.txt", "r")], {}, {}, 1, 0
for i, line in enumerate(f + [""]):
    if line.startswith("Starting items"): mitems, moperation, mtest, mtrue, mfalse = [(int)(item.strip()) for item in line.split(":")[1].split(",")], f[i + 1].split(":")[1].strip(), (int)(f[i + 2].split()[-1]), (int)(f[i + 3].split()[-1]), (int)(f[i + 4].split()[-1])
    elif len(line) == 0: monkeysa[mnum], monkeysb[mnum], mnum, modulus = (mitems, moperation, mtest, mtrue, mfalse), (mitems.copy(), moperation, mtest, mtrue, mfalse), mnum + 1, modulus * mtest
for run in range(2):
    monkeys, active = monkeysa if run == 0 else monkeysb, [0] * len(monkeysa)
    for _ in range(10000 if run == 1 else 20):
        for k, monkey in monkeys.items():
            for item in monkey[0]:
                item = item * item if monkey[1].split()[-1] == "old" else item * (int)( monkey[1].split()[-1]) if "*" in monkey[1] else item + (int)( monkey[1].split()[-1])
                item, active[k] = item % modulus if run == 1 else item // 3, active[k] + 1
                monkeys[monkey[3 if item % monkey[2] == 0 else 4]][0].append(item)
            monkey[0].clear()
    print(max(active) * max([x for x in active if x < max(active)]))
