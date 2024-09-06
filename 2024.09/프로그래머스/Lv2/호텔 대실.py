# 이차원 배열 활용하깅
from collections import deque

def solution(book_time):
    
    book_time.sort()
    print(book_time)
    
    hotel = deque()
    
    # 분으로 치환해서 생각
    for i in range(len(book_time)):
        b_start = int(book_time[i][0][:2]) * 60 + int(book_time[i][0][3:])
        b_end = int(book_time[i][1][:2]) * 60 + int(book_time[i][1][3:])
        hotel = deque(sorted(hotel))
        # 만약 추가된 방이 하나도 없다면 추가해준다
        if len(hotel) == 0:
            hotel.append(b_end)
        else: # 아니라면 호텔방과 비교 시작
            for j in range(len(hotel)): # 호텔방 하나씩 탐색
                # 호텔 방 + 청소시간 <= 예약시간 -> 조건만족! 원래꺼 지우고 넣기
                if hotel[j] + 10 <= b_start:
                    del hotel[j]
                    hotel.append(b_end)
                    break
                else: # 아니라면 그냥 추가
                    hotel.append(b_end)
                    break
                
    return len(hotel)
