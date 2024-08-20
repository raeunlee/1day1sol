
import itertools

def solution(orders, course):
    answer = []
    
    for c in course:
        count = {}
        comb = []
        max_order = []
        
        for o in orders:
            o_comb = itertools.combinations(list(o), c)
            
            for o_c in o_comb:
                o_c_str = "".join(sorted(o_c))
                
                if o_c_str in count:
                    count[o_c_str] += 1
                else:
                    count[o_c_str] = 1
        
        for key, value in count.items():
            if value == max(count.values()) and value >= 2:
                max_order.append(key)
    
        answer.extend(max_order)
    answer.sort()
    return answer
