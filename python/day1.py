x, elves = [line for line in open("../input/day1.txt", "r")], []
for c in "".join(x).replace("\n", " ").split("  "):
    elves.append(sum([int(i) for i in c.strip().split(" ")]))
print(max(elves))
print(sum(sorted(elves)[-3:]))
