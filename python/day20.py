from collections import deque
class nr: 
    def __init__(self, val): self.val = val
f = [(int)(line.strip()) for line in open("../input/day20.txt", "r")]
for run in range(2):
    numbers = deque(nr(number * (811589153 if run == 1 else 1)) for number in f)
    premixed, res = list(numbers), 0
    for _ in range(10 if run == 1 else 1):
        for number in premixed:
            numbers.rotate(-numbers.index(number))
            numbers.popleft()
            numbers.rotate(-number.val)
            numbers.insert(0, number)
    while numbers[0].val != 0: numbers.rotate(-1)
    for _ in range(3):
        numbers.rotate(-1000)
        res += numbers[0].val
    print(res)
