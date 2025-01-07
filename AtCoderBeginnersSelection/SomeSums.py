input = list(map(int, input().split()))

n = input[0]
a = input[1]
b = input[2]

r = n + 1

A = []
cnt = 0
sumall = 0

for i in range(1, r):
    sum = 0
    A = [int(c) for c in list(str(n))]
    
    for j in range(len(A)):
       sum += A[j]

    if a <= sum <= b:
       sumall += n
    
    if n == 1:
       break
    else:
        n -= 1
    
print(sumall)