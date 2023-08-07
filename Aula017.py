num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não tem o número 4')
num.remove(2)
print(num)
print(f'Esta lista tem {len(num)} elementos.')