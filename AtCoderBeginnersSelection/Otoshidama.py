a = list(map(int, input().split()))
n = a[0]
y = a[1]

cnt = 0

for i in range(0, n+1):
    for j in range(0, n+1):
        k = n - i - j # n == (i + j + k)になるので、iとjが決まればkも決まる
        if k >=0 and n == (i + j + k) and y == (10000*i + 5000*j + 1000*k):
            print(f'{i} {j} {k}')
            cnt += 1
            break
    else:
        continue
    break

if cnt == 0:
    print('-1 -1 -1')