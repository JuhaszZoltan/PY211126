import random
# adott egy 10 db [0; 10) közötti véletlen számot tartalmazó lista
# tartalmaz-e 3mal osztható elemet

# kiindulási állapot:
t = []
for n in range(10): t.append(random.randrange(1, 10))
print(t)

i = 0
while i < len(t) and t[i] % 3 != 0:
    i += 1
if i < len(t): print('van a t-ben 3mal osztható elem')
else: print('nincs a t-ben 3mal osztható elem')