import sys

line = str(input())
divide = ['dream','dreamer','erase','eraser']

# 入力文字列、定数をそれぞれ左右反対にする
line = line[::-1]
for i in range(len(divide)):
    divide[i] = divide[i][::-1]











# if len(list(lint)) <= 4:
#     print('NO')
#     sys.exit(0)

# flg = True

# while flg:
#     if lint[0:5] == 'dream' or lint[0:5] == 'erase':
#         lint = lint[5:]
    
#     if lint == '':
#         print('YES')
#         flg = False
#         break

#     if len(list(lint)) <= 4:
#         print('NO')
#         flg = False
#         break

#     if lint[0:6] == 'dreamer' or lint[0:6] == 'eraser':
#         lint = lint[6:]

#     if lint == '':
#         print('YES')
#         flg = False
#         break

#     if len(list(lint)) <= 4:
#         print('NO')
#         flg = False
#         break