t = [2, 3, 4, 46, 7, 11, 43, 2]

c = 0
for szam in t:
    if szam % 2 == 0: c += 1

print(f'{c} db páros elem van a t-ben')