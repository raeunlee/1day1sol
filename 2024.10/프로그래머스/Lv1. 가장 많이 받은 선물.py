def solution(friends, gifts):
    answer = 0
    
    # 이름과 인덱스
    f = {}
    
    # 이차원 배열
    ff = [[0] * len(friends) for i in range(len(friends))]

    # 각 이름마다 idx 부여 
    idx = 0
    for friend in friends:
        f[friend] = idx
        idx += 1
        
    print("인덱스 값과 이름", f)
    
    # 선물 내역 완탐하여 ff에 채워넣기
    
    # 선물지수
    l = [0] * len(friends)
    
    for gift in gifts:
        a, b = gift.split(" ") # 준사람, 받은사람
        ff[f[a]][f[b]] += 1
        l[f[a]] += 1
        l[f[b]] -= 1

    print("선물지수", l)
    
    # 2차원 선물 배열
    print(ff)    
    
    p = {}
    for friend in friends:
        p[friend] = 0
        
    # 인덱스값으로 이름 찾기
    reversed_f= dict(map(reversed,f.items()))
    print(reversed_f)
    
    # 준 사람 기준으로 선물 받을지 말지
    for i in range(len(ff)): # 준사람 기준
        for j in range(len(ff)):
            if i == j: # 자기자신에게 줄수없음
                continue
        
            print(ff[i][j], ff[j][i]) 
            # 한 사람 한테 두번 받을 수 없음

            # 선물 주고받은 기록이 있다면
            if (ff[i][j] != 0 or ff[j][i] != 0) and (ff[i][j] != ff[j][i]):
                if ff[i][j] > ff[j][i]:
                    print("줘서 +1")
                    p[reversed_f[i]] += 1
               
            
            # 선물 주고 받은 기록이 1도 없거나 주고 받은 수가 같다면?
            elif (ff[i][j] == 0 and ff[j][i] == 0) or (ff[i][j] == ff[j][i]):  
                # 선물지수가 큰쪽이 선물 받음
                print("선물지수 비교", l[i], l[j])
                if l[i] > l[j]:
                    p[reversed_f[i]] += 1
            
            answer = max(p.values())
            
    return answer
