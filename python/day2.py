def score(me, opponent):
    if me == conv[opponent]: return 3 + game[me][0]
    if me == game[conv[opponent]][1]: return 6 + game[me][0]
    return game[me][0]

input, game, conv, a, b = [line.strip() for line in open("../input/day2.txt", "r")], {"X": [1, "Y", "Z"], "Y": [2, "Z", "X"], "Z": [3, "X", "Y"]}, {"A": "X", "B": "Y", "C": "Z"}, 0, 0

for i, j in [l.split(" ") for l in input]:
    a += score(j,i)
    match j:
        case "Y": b += score(conv[i], i)
        case "Z": b += score(game[conv[i]][1], i)
        case "X": b += score(game[conv[i]][2], i)
print(a, b)
