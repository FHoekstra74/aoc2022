def calc (inst, partb, humn):
    if partb: inst["humn"] = humn
    while True:
        for k, v in [(key,value.split()) for (key,value) in inst.items() if type(value) is str and type(inst[value.split()[0]]) is not str and type(inst[value.split()[2]]) is not str]:
            inst[k] = inst[v[0]] + inst[v[2]] if v[1] == "+" else inst[v[0]] - inst[v[2]] if v[1] == "-" else inst[v[0]] * inst[v[2]] if v[1] == "*" else inst[v[0]] / inst[v[2]]
            if k == "root": return inst[v[0]] - inst[v[2]] if partb else inst[k]
inst, mini, maxi, res = {h[0]: (int)(h[1].strip()) if h[1].strip().isnumeric() else h[1].strip() for h in [l.strip().split(":") for l in open("../input/day21.txt", "r")]}, 0, 10000000000000, 1
print("a:", (int)(calc(inst.copy(), False, 0)))
while res != 0:
    res = calc(inst.copy(), True, (mini + maxi) // 2)
    if res == 0: print("b:", (mini + maxi) // 2)
    mini, maxi = ((mini + maxi) // 2, maxi) if res > 0 else (mini, (mini + maxi) // 2)
    