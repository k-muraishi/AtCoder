n = int(input())
a = list(map(int, input().split()))
char = input()
total = 0

for i in range(2):
    total += a[i]

total += n 

print(f'{total} {char}')