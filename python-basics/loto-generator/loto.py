import random

numere_6din49 = random.sample(range(1, 50), 6)
print("Numere 6/49 " + str(numere_6din49))

numere_nrJoker = random.sample(range(1, 46), 5)
numere_joker = random.sample(range(1, 21),1)
print("Numere Joker " + str(numere_nrJoker))
print("Joker " + str(numere_joker))

numere_5din40 = random.sample(range(1, 41), 5)
print("Numere 5/49 " + str(numere_5din40))
