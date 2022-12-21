def calc (inst, mode):
    while True:
        for k,v in inst.items():
            if type(v) is str:
                i = v.split()
                if type(inst[i[0]]) is not str and type(inst[i[2]]) is not str:
                    num1, num2, res  = inst[i[0]], inst[i[2]], 0
                    if i[1] == "+": res = num1 + num2
                    elif i[1] == "-": res = num1 - num2
                    elif i[1] == "*": res = num1 * num2
                    elif i[1] == "/": res = num1 / num2
                    inst[k] = res
                    if k == "root": return res if mode == 1 else num1 - num2

f, inst = [line.strip() for line in open("../input/day21.txt", "r")], {}
for line in f:
    h = line.split(":")
    inst[h[0]] = (int)(h[1].strip()) if h[1].strip().isnumeric() else h[1].strip()
print("a:", calc(inst.copy(),1))
mini, maxi = 0, 10000000000000
while True:
    mid = (mini + maxi) // 2
    cp = inst.copy()
    cp["humn"] = mid
    res = calc(cp, 2)
    if res > 0: mini = mid
    elif res < 0: maxi = mid
    else:
        print("b:", mid)
        break
    