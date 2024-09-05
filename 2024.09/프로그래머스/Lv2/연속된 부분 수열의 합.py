# 오름차순 정렬 수열, 부분 수열 찾기

def solution(sequence, k):
    # 매번 sum 구하지 않고 + 투포인터 사용
    answer = []
    l, r = 0, 0 # 왼, 오
    n = len(sequence)
    total = sequence[0] # 합계
    
    # 왼, 오 둘다 전체 범위보다 작을 때
    while l < n and r < n:   
        if total < k: 
            r += 1
            if r < n:
                total += sequence[r]
        else: # 합계가 같거나 아님 더 클경우
            if total == k: # 같으면 답변에 더해줌
                answer.append([l,r])
            total -= sequence[l] # 안 같으면 왼쪽꺼 빼주고 +1 
            l += 1
    
    # 부분 수열 여러 개인 경우 길이가 짧은 수열, 짧은 수열이 여러개인 경우 시작 인덱스가 작은 경우
    answer.sort(key = lambda x : (x[1]-x[0] , x[0]))
    return answer[0]
 
# 투 포인터, sum 활용 - 시간초과 
#     answer = []
#     r, l = 1, 0
#     while r >= l:
#         tmp = sequence[l:r]
#         print(tmp)
#         if r >= n+1:
#             break   
            
#         if sum(tmp) == k:
#             answer.append([l,r-1])
#             r += 1
#             l += 1     
#         else:
#             if sum(tmp) < k:
#                 r += 1
#             elif sum(tmp) >= k:
#                 l += 1
                
#     answer.sort(key = lambda x : (x[1]-x[0] , x[0]))
#     print(answer)
#     return answer[0]
 
    
    
    # 1트 - 완탐으로 무식하게 찾음
    # for i in range(n+1):
    #     for j in range(i, n+1):
    #         tmp = sequence[i:j]
    #         if sum(tmp) == k:
    #             answer.append([i, j-1])
    # answer.sort(key = lambda x : (x[1]-x[0]))
    # print(answer)
    # return answer[0]
