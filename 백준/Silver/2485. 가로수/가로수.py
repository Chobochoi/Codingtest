import math

N = int(input())
positions = [int(input()) for _ in range(N)]
positions.sort()

# 간격들의 GCD 계산
gaps = [positions[i+1] - positions[i] for i in range(N-1)]
final_gap = gaps[0]
for gap in gaps[1:]:
    final_gap = math.gcd(final_gap, gap)

# 답 계산
result = (positions[-1] - positions[0]) // final_gap - N + 1
print(result)