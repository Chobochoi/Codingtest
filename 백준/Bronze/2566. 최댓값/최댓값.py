import sys

input = sys.stdin.readline

ST = []
for _ in range(9):
    row = list(map(int, input().split()))
    ST.append(row)

max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= ST[row][col]:    
            max_row, max_col = row +1, col +1
            max_num = ST[row][col]
            
print(max_num)
print(max_row, max_col)
