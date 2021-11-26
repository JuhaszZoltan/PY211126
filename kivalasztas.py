t = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

# kiválasztás: akkor használom, ha BIZTOSAN benne van az adatszerkezetben a keresett <T> tulajdonságú elem

i = 0
while t[i] != pow(2, 5):
    i += 1

print(f'kettő 5. hatvány a t {i} indexű eleme {t[i]}')