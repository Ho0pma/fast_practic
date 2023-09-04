# l = [3, 2, 1]
# print(l.__contains__(4))
# print(1 in l)
# l.__reversed__()
# print(l)
#
# s = [5, 6, 7]
#
# l.extend(s)
# print(l)
# print(l + s)
#
# del l[1]
# print(l)
#
# l = ['1', '2', '3']
# k = ' '.join(l)
# print(k)
# print(type(k))
# lst = k.split()
# print(type(lst))


# s = '1, 2, 3'
# e = s.encode()
# print(e)
# print(e.decode())

# как проверить хэшируемый объект или нет
lst = [1, 2, 3]
# print(hash(lst)) # выдаст ошибку, тк список изменяемый объект
print(hash(tuple(lst))) # 529344067295497451 -> hash тк кортеж - неизменяемый объект
# print(hash(set(lst))) # выдаст ошибку, тк список изменяемый объект
print(hash(frozenset(lst)))  # -272375401224217160 тк такой тип сета - неизменяемый
print(hash('blablabla')) # тоже все гут

s1 = {1, 2, 3, 4, 5}
s2 = {5, 7, 8, 9}
s1.symmetric_difference_update(s2)
print(s1)

d = {1: '1'}
print(d.get(2))

from collections import OrderedDict, Counter

print(OrderedDict.fromkeys([1, 2, 3, 3], 2))
print(Counter([1, 2, 3, 3]))