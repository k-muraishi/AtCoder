import sys

line = str(input())
divide = ['dream','dreamer','erase','eraser']

# 入力文字列、定数をそれぞれ左右反対にする
# すべて文字を抽出できる文字列が与えられたら後ろからでも最終的にすべて抽出できる
# 逆の場合、後ろからだと抽出できず最初のループでflg2がfalseのままとなる

line = line[::-1]
for i in range(len(divide)):
    divide[i] = divide[i][::-1]

flg = True

while(flg):
    flg2 = False
    for i in range(len(divide)):
        d = divide[i]
        dline = line[0:len(d)]
        if line[0:len(d)] == d:
            line = line[len(d):]
            flg2 = True
            break

    if flg2 == False or len(line) == 0:
        flg = False

if len(line) == 0:
    print('YES')
else:
    print('NO')