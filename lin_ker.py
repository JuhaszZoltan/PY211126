t = ['cica', 'kutya', 'whisky', 'dákó', 'ananász']
keresett_szo = input('ezt a szót keresem: ')

i = 0
while i < len(t) and keresett_szo != t[i]:
    i += 1

if i < len(t):
    print('van találat, a keresett szó benne van a t-ben')
    print(f'a {i} indexű elem (vagyis az {i + 1}. elem)')
else:
    print('a keresett szó nem szerepel a t-ben')