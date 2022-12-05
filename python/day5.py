f = [line for line in open("../input/day5.txt", "r")]
nrstacks, stacka, stackb, a, b = int(len(f[0]) / 4), [], [], "", ""
for i in range(nrstacks): stacka.append("")
for l in f:
    if "[" in l:
        for i in range(nrstacks): stacka[i] += l[i * 4 + 1].strip()
    elif len(l.strip()) == 0: stackb = stacka.copy()
    elif l.startswith("move"):
        nr, frm, to, moveb = int(l.split(" ")[1]), int(l.split(" ")[3]), int(l.split(" ")[5]), ""
        for i in range(nr):
            stacka[to - 1] = stacka[frm - 1][0] + stacka[to - 1]
            moveb += stackb[frm - 1][0]
            stacka[frm - 1], stackb[frm - 1] = stacka[frm - 1][1:], stackb[frm - 1][1:]
        stackb[to - 1] = moveb + stackb[to - 1]
print("".join([stacka[i][0] for i in range(nrstacks)]), "".join([stackb[i][0] for i in range(nrstacks)]))
