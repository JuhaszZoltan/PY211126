class Diak:
    def __init__(self, nev, kor):
        self.Nev = nev
        self.Kor = kor

diakok = []

sorsz = 1
while len(diakok) < 10:
    nev = input(f'{sorsz}. diák neve: ')
    if nev == '': break
    kor = int(input(f'{sorsz}. diák életkora: '))
    diakok.append(Diak(nev, kor))
    sorsz += 1

# átlagéletkor
sum = 0
for d in diakok:
    sum += d.Kor
print(f'átlagéletkor: {sum / len(diakok)}')
# ki a legidősebb diák?
maxi = 0
for i in range(1, len(diakok)):
    if diakok[i].Kor > diakok[maxi].Kor:
        maxi = i
# print(f'a legidősebb diák {diakok[maxi].Nev}, ő {diakok[maxi].Kor} éves')

# -> kik a legidősebb diákok
print(f'{diakok[maxi].Kor} éves diákok listája: ')
for d in diakok:
    if d.Kor == diakok[maxi].Kor:
        print(f'  {d.Nev}')