from collections import deque
def solution(plans):
    answer = []
    
    # 새로 시작해야되는 과제
    arr = []
    # 기존에 진행중이던 과제
    st = []

    for plan in plans:
        subject, start, time = plan
        start_min = int(start[:2])*60 + int(start[3:])
        arr.append((subject, start_min, int(time)))
    
    arr.sort(key = lambda x : x[1])

    for i in range(len(arr)-1):
        n, s, t = arr[i]
        if s + t <= arr[i+1][1]:
            answer.append(n)
            tot = arr[i+1][1] - s - t
            while st:
                name, time = st.pop()
                if tot >= time:
                    tot -= time
                    answer.append(name)
                else:
                    st.append((name, time - tot))
                    break

        else:
            st.append((n, t - (arr[i+1][1] - s)))
    answer.append(arr[-1][0])

    while st:
        answer.append(st.pop()[0])
    return answer
