from itertools import combinations

def main():
    # 9명의 난쟁이 키 입력받기
    heights = []
    for _ in range(9):
        heights.append(int(input()))
    
    # 전체 키의 합계
    total_sum = sum(heights)
    
    # 제거해야 할 2명의 키 합 = 전체 합 - 100
    # 왜냐하면: (9명 합) - (2명 합) = 7명 합 = 100
    target_sum = total_sum - 100
    
    # 9명 중에서 2명을 선택하는 모든 조합 확인
    # C++에서 이중 반복문으로 구현했을 로직을 combinations로 간단히 처리
    for two_dwarfs in combinations(heights, 2):
        # 선택된 2명의 키 합이 target_sum과 같다면
        if sum(two_dwarfs) == target_sum:
            # 이 2명을 제외한 나머지 7명이 정답
            seven_dwarfs = []
            temp_heights = heights.copy()  # 원본 보존
            
            # 제거할 2명을 리스트에서 제거
            for dwarf in two_dwarfs:
                temp_heights.remove(dwarf)
            
            seven_dwarfs = temp_heights
            break
    
    # 오름차순 정렬 후 출력
    seven_dwarfs.sort()
    for height in seven_dwarfs:
        print(height)

if __name__ == "__main__":
    main()