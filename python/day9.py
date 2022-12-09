f, rope, hposb, hposa = [line.strip() for line in open("../input/day9.txt", "r")], [(0, 0)] * 10, set(), set()
vectors = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for dir, steps in [l.split() for l in f]:
    for i in range(int(steps)):
        rope[0] = (rope[0][0] + vectors[dir][0], rope[0][1] + vectors[dir][1])
        for i in range(len(rope) -1):
            newx, newy = rope[i + 1][0], rope[i + 1][1]
            if rope[i][0] - rope[i + 1][0] >= 2 and rope[i][1] == rope[i + 1][1]: newx += 1
            elif rope[i + 1][0] - rope[i][0] >= 2 and rope[i][1] == rope[i + 1][1]: newx -= 1
            elif rope[i][1] - rope[i + 1][1] >= 2 and rope[i][0] == rope[i + 1][0]: newy += 1
            elif rope[i + 1][1] - rope[i][1] >= 2 and rope[i][0] == rope[i + 1][0]: newy -= 1
            elif rope[i][0] - rope[i + 1][0] >= 2:
                newx += 1
                newy += 1 if rope[i + 1][1] < rope[i][1] else -1
            elif rope[i + 1][0] - rope[i][0] >= 2:
                newx -= 1
                newy += 1 if rope[i + 1][1] < rope[i][1] else -1
            elif rope[i][1] - rope[i + 1][1] >= 2:
                newy += 1
                newx += 1 if rope[i + 1][0] < rope[i][0] else -1
            elif rope[i + 1][1] - rope[i][1] >= 2:
                newy -= 1
                newx += 1 if rope[i + 1][0] < rope[i][0] else -1
            if rope[i + 1] != (newx, newy):
             #   print ("following", rope[i], ":", rope[i + 1], " becomes ", (newx, newy))
                rope[i + 1] = (newx, newy)
        if rope[1] not in hposa: hposa.add(rope[1])
        if rope[-1] not in hposb: hposb.add(rope[-1])
print(len(hposa))
print(len(hposb))
