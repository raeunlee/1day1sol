def solution(record):
    answer = []
    
    # 아이디, 이름 매칭
    id_name = {}
    # 아이디, 들어왔는지 나갔는지 -> 중복가능
    come_out = []
    
    for r in record:
        
        tmp = list(r.split(" "))

        
        state = tmp[0]
        user_id = tmp[1]
        
        if state == "Enter":
            if user_id in id_name:
                id_name[user_id] = tmp[2]
            else:
                id_name[user_id] = tmp[2]
            come_out.append([user_id, state])

        elif state == "Leave":
            come_out.append([user_id, state])
        
        elif state == "Change":
            if user_id in id_name:
                id_name[user_id] = tmp[2]
    
    for each in come_out:
        tmp=""
        if each[1] == "Enter":
            tmp += "님이 들어왔습니다."
        else:
            tmp += "님이 나갔습니다."
        answer.append(id_name.get(each[0])+tmp)
            
        
    return answer
