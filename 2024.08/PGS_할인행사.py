def solution(want, number, discount):
    answer = 0
    mydict = {}
    
    for i in range(len(want)):
        x = want[i]
        y = number[i]
        mydict[x] = y    
    print("want", mydict)
    
    cycle = len(discount) - 9 # 10씩 계산
    
    for j in range(cycle):
        #print("cycle", j)
        tmp = mydict.copy()
        for k in range(j, j+10):
            if discount[k] in mydict:
                tmp[discount[k]] -= 1
        #print("after cycle", tmp)
        dict_sum = 0
        for t in tmp:
            dict_sum += tmp[t]
        if dict_sum == 0 and all(value <= 0 for value in tmp.values()):
            answer += 1

    return answer