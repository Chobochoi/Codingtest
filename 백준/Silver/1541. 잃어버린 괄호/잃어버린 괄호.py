expression = input()
parts = expression.split('-')
result = sum(int(x) for x in parts[0].split('+')) - sum(sum(int(x) for x in part.split('+')) for part in parts[1:])
print(result)