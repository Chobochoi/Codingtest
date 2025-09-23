N, M = map(int, input().split())

K = []

for i in range(1, N+1):
    K.append(int(input()))    

K.sort(reverse = True)

total = 0

for coin in K:
    if M >= coin:
        total += M // coin
        M %= coin
        if M <= 0:
            break
        
print(total)