t = [4, 76, 11, 3, 32, 6]

mini = 0
maxi = 0
for i in range(1, len(t)):
    if t[i] < t[mini]: mini = i
    if t[i] > t[maxi]: maxi = i

print(f'a legkisebb elem a t {mini} indexű eleme, azaz a {t[mini]}, ez a t {mini + 1}. eleme')
print(f'a legnagyobb elem a t {maxi} indexű eleme, azaz a {t[maxi]}, ami a t {maxi + 1}. eleme.')



