import sys

input = sys.stdin.readline

N = int(input().rstrip())

total_count = 0
user_set = set()

for _ in range(N):
    chat = input().rstrip()
    
    if chat == "ENTER":
        total_count += len(user_set)
        user_set.clear()
    else:
        user_set.add(chat)

total_count += len(user_set)

print(total_count)
