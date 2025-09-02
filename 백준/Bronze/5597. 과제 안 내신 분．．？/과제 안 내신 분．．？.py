import sys
input = sys.stdin.readline

ST = []

for i in range(30):
    ST.append(i+1)  
    
for value in range(1, 29):
    M = int(input())
    ST.remove(M)

print(min(ST))
print(max(ST))