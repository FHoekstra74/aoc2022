import functools

def compare2(left, right): return compare(left, right, False, 0)
def compare(left, right, debug, level):
    if debug: print("-", " " * level,  "Compare", left, "vs", right)
    if type(left) is list and type(right) is list:
        found = False
        for l in range(min(len(left), len(right))):
            res = compare(left[l], right[l], debug, level+1)
            if res in [-1, 0]:
                found = True 
                return res
        if not found:
            if len(left) > len(right): return -1
            elif len(left) < len(right): return 0
            else: return 99
    elif type(left) is list: return compare(left, [right], debug, level + 1)
    elif type(right) is list: return compare([left], right, debug, level + 1)
    else: return 0 if left < right else -1 if left > right else 99

#compare ([[4,4],4,4], [[4,4],4,4,4], True, 0)
#compare ([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9], True, 0)
f, a = [eval(l) for l in [line.strip() for line in open("../input/day13.txt", "r")] if len(l) > 0], 0
for k in range(0, len(f) - 1, 2): a += (k+2)//2 if compare(f[k], f[k + 1], False, 0) == 0 else 0
f.append([[2]])
f.append([[6]])
f.sort(key = functools.cmp_to_key(compare2), reverse = True)
b = (f.index([[2]]) + 1) * (f.index([[6]]) + 1)
print(a, b)