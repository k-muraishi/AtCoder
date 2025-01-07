n = int(input())
a = list(map(int, input().split()))

cnt = 0
flg = True

while flg:
    for i in range(n):
        amr = a[i] % 2
        if amr != 0:
            flg = False
            break
        else:
            a[i] = a[i]/2
    
    if flg:
        cnt += 1

print(cnt)