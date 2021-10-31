# 13.1

# def multiply(*nums):
#     ls = []
#     for num in nums:
#         summ = 0
#         while num != 0:
#             last = num % 10
#             summ += last
#             num = num // 10
#         ls.append(summ)
#     print(sorted(ls))
# multiply(965, 582, 23, 8, 695210)

# 13.2
#
# def f(x):
#     if x <= -2:
#         last = 1 - (x - 2)**2
#     if x -2 < x <= 2:
#         last = -x / 2
#     if 2 < x:
#         last = (x - 2)** 2 + 1
#     return last
# print(f(4.5))

# 13.3

def calc(*nums):
    ls = []
    for num in nums:
        if num % 2 == 0:
            ls.append(num // 2)
    return ls
print(calc(852, 85, 784, 58))




