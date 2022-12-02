def score(me, opponent):
    round = game[me][0]
    if me == conv[opponent]: round += 3
    elif me == game[conv[opponent]][1]: round += 6
    return round

input, game, conv, b = [line.strip() for line in open("../input/day2.txt", "r")], {"X": [1, "Y", "Z"], "Y": [2, "Z", "X"], "Z": [3, "X", "Y"]}, {"A": "X", "B": "Y", "C": "Z"}, 0

print(sum([score(l.split(" ")[1], l.split(" ")[0]) for l in input]))
for l in input:
    opponent, outcome = l.split(" ")[0], l.split(" ")[1]
    match outcome:
        case "Y": me = conv[opponent]
        case "Z": me = game[conv[opponent]][1]
        case "X": me = game[conv[opponent]][2]
    b += score(me, opponent)
print(b)
