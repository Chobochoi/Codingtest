parts = input().split('-')

sum_parts = []

for i in parts:
    temp = list(map(int, i.split('+')))
    sum_parts.append(sum(temp))
    
result = sum_parts[0]

for i in sum_parts[1:]:
    result -= i
    
print(result)