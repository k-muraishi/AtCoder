import sys

lint = str(input())

if len(list(lint)) <= 4:
    print('NO')
    sys.exit(0)

flg = True

while flg:
    if lint[0:5] == 'dream' or lint[0:5] == 'erase':
        lint = lint[5:]
    
    if lint == '':
        print('YES')
        flg = False
        break

    if len(list(lint)) <= 4:
        print('NO')
        flg = False
        break

    if lint[0:6] == 'dreamer' or lint[0:6] == 'eraser':
        lint = lint[6:]

    if lint == '':
        print('YES')
        flg = False
        break

    if len(list(lint)) <= 4:
        print('NO')
        flg = False
        break