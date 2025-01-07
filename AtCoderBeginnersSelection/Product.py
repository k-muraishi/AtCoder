a = list(map(int, input().split()))

for i in range(2):
    if i == 1:
        first  = a[i]
    else:
        second = a[i]

seki = first * second
amari = seki % 2

if amari != 0:
    print('Odd')
else :
    print('Even')