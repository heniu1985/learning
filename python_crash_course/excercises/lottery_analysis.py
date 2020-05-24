from random import choice, randint

jackpot = [i for i in range(1, 50)]
jackpot_copy = jackpot[:]

my_ticket = [5, 6, 9, 10, 14, 20]
draw = []
l = 0
i = 0

while True:

    while i <= 6:
        n = choice(jackpot_copy)
        draw.append(n)
        jackpot_copy.remove(n)
        i += 1

    if sorted(draw) != my_ticket:
        l += 1
        draw = []
        jackpot_copy = jackpot[:]        
    else:        
        print("Wygrałeś")
        print(f"Potrzebowałeś do tego {l} losowań.")
        break