from collections import deque

def solution(queue1, queue2):

    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    count, max_count = 0, len(q1) * 3
    # 최대카운트 : q1을 모두 q2로 옮기고 또 다시 q1으로옮기는 모든과정 len(q1) * 3
    
    if s1 == s2:
        return 0
    elif (s1 + s2) % 2 == 1 :
        return -1
    
    while True:
        if s1 > s2:
            now = q1.popleft()
            q2.append(now)
            s1 -= now
            s2 += now
            count += 1
        elif s2 > s1:
            now = q2.popleft()
            q1.append(now)
            s2 -= now
            s1 += now
            count += 1
        else: #같으면
            break
        if count == max_count:
            return -1
            
     
    return count

 
