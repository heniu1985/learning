from random import choice

jackpot = [8, 5, 4, 7, 3, 1, 4, 13, 55, 32, "s", "g", "w", "q", "i"]

i = 0
draw = []

while i <= 4:
    l = choice(jackpot)
    draw.append(l)
    i += 1

print("Kupon zawierający następujące liczby lub litery wygrywa:")
for i in draw:
    print(f"- {i}")