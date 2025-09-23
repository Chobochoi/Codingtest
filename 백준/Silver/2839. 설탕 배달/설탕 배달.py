N = int(input())

# 봉지는 3kg, 5kg 두 종류
total = 0

while N >= 0:
    if N % 5 == 0:
        total += N // 5
        print(total)
        break
    N -= 3
    total += 1
    
else: 
    print(-1)