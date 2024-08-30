from collections import deque

def solution(bandage, health, attacks):
    answer = health
    
    now = 1
    skill = 0

    while len(attacks) > 0:
        if now == attacks[0][0]:
            answer -= attacks[0][1]
            skill = 0
            attacks.pop(0)
            if answer <= 0 :
                answer = -1
                break
        else:
            answer += bandage[1]
            if answer >= health:
                answer = health
            skill += 1
            if skill == bandage[0]: # 연속기준 만족하면
                answer += bandage[2] # 추가 회복한다
                if answer >= health:
                    answer = health
                skill = 0 # 연속 초기화
        now += 1
        
    return answer 
                
