import random

goal = [
    0b111000000, 0b000111000, 0b000000111, 0b100100100,
    0b010010010, 0b001001001, 0b100010001, 0b001010100
]

def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

def play(p1, p2):
    if check(p2):
        print([bin(p1), bin(p2)])
        return

    board = p1 | p2
    if board == 0b111111111:
        print([bin(p1), bin(p2)])
        return

    w = [i for i in range(9) if (board & (1 << i)) == 0]

    r = random.choice(w)
    play(p2, p1 | (1 << r))

play(0, 0)
