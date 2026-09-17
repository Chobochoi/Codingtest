from collections import defaultdict

def solution(genres, plays):
    # 1. 장르별 총 재생횟수 집계
    genre_total = defaultdict(int)
    for g, p in zip(genres, plays):
        genre_total[g] += p

    # 2. 장르별로 (인덱스, 재생횟수) 모아두기
    genre_songs = defaultdict(list)
    for idx, (g, p) in enumerate(zip(genres, plays)):
        genre_songs[g].append((idx, p))

    # 3. 장르를 총 재생횟수 내림차순 정렬
    sorted_genres = sorted(genre_total.keys(), key=lambda g: -genre_total[g])

    answer = []
    for g in sorted_genres:
        # 4. 장르 내에서 재생횟수 내림차순 정렬 (동점이면 인덱스 오름차순)
        songs = sorted(genre_songs[g], key=lambda x: (-x[1], x[0]))
        # 5. 최대 2곡까지만 선택
        for idx, p in songs[:2]:
            answer.append(idx)

    return answer