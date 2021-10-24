import random

# 10_7
#
# s = input().split()
# with open('file.txt', 'w') as f:
#     for i in s:
#         f.write(i + '\n')

# 10_8
#
# a = [5, True, 'abc']
# with open('file.txt', 'w') as f:
#     for i in a:
#         f.write(str(i) + '\n')

# # 10_9

a = [random.randint(1, 101) for i in range(10)]
list = []
for i in a:
    if i % 2 != 0:
        list.append(i)
with open('file.txt', 'w') as f:
    for y in list:
        f.write(str(y) + '\n')
print(list)

