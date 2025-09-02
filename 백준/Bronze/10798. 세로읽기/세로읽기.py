import sys
#input = sys.stdin.readline

ST = []

for value in range(5):
    ST.append(input())

max_length = max(len(st)for st in ST)

result = ''

for col in range(max_length):
    for row in range(5):
        if col < len(ST[row]):
            result += ST[row][col]
    
print(result)