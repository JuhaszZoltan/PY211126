# Írjunk programot, amely egy adott értelmes szövegről eldönti, hogy több mondatból áll-e!

szoveg = input("írj be egy szöveget: ")

db = 0
i = 0
while i < len(szoveg) and db < 2:
    if szoveg[i] in ['.', '!', '?']:
        db += 1
    i += 1
if db > 1: print('több mondat')
else: print('csak egy mondat')