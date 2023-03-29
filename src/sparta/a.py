# a = 1
# b = a
# #
#
import copy

c = 2
d = copy.deepcopy(c) + 2

print(id(c))
print(id(d))



# a = [[1, 2], [3, 4]]
# b = copy.deepcopy(a)
# a[1].pop()
#
# print(a)
# print(id(a))
# print(b)
# print(id(b))
