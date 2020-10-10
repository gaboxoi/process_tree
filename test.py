# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "yearr": 1964,
# }

# def test():
#     a = [1]
#     add(a)
#     print(a)
#
# def add(x):
#     x.append(2)
#
# test()

# lit = [1,2,3]
#
# thisdict.update({"abc" : lit})
#
# print(thisdict.get("abc"))

#
# b = 0
#
# def test():
#     a = 0
#     if(b == 0):
#         a = 2
#     return a
# print(test())
from BasicStack import Stack
stack = Stack([1,2,3])
print(stack.items)
rev = stack.to_list()
print(rev)
print(stack.items)
