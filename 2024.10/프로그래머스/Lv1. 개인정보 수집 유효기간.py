def solution(today, terms, privacies):
    term = {}
    answer = []
    for each in terms:
        kind, month = each.split(" ")
        term[kind] = int(month)
   
    n_year, n_month, n_day = today.split(".")
    n_year = int(n_year)
    n_month = int(n_month)
    n_day = int(n_day)
    # 오늘 날
    print("오늘", n_year, n_month, n_day)
    
    
    for i in range(len(privacies)):
  
        p_year = int(privacies[i][:4])
        p_month = int(privacies[i][5:7])
        p_day = int(privacies[i][8:10])

        p = int(term[privacies[i][-1:]])
        
        month_count = 0
        year_count = 0
        tmp_day = p_day + (28 * p) - 1 # 현재 날짜 + 남은 달 * 28 개월
        p_day = tmp_day % 28 # 지금 날짜
        
        if p_day == 0:
            p_day = 28 
            month_count += 1
            
        tmp_month = p_month + (tmp_day // 28) - month_count # 임시 달 
        p_month = tmp_month % 12
        
        if p_month == 0:
            p_month = 12
            year_count += 1
        
        p_year = p_year + tmp_month // 12 - year_count

        print(i, "보정 후", p_year, p_month, p_day)
        
        # 오늘이 연도가 더 크면
        if p_year < n_year:
            answer.append(i+1)
        elif p_year == n_year:
            if p_month < n_month:
                answer.append(i+1)
            elif p_month == n_month:
                if p_day < n_day:
                    answer.append(i+1)
        
        
    
    return answer
