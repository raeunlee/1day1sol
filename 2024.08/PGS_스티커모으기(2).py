def solution(sticker):
    
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0], sticker[1])

    dp1 = []
    
    dp1.append(sticker[0])
    dp1.append(sticker[0])

    for i in range(2, len(sticker) - 1):
        dp1.append(max(dp1[i-1], dp1[i-2] + sticker[i]))
           
    print(dp1)
    
    dp2 = []
    
    dp2.append(0)
    dp2.append(sticker[1])
    
    for i in range(2, len(sticker)):
        dp2.append(max(dp2[i-1], dp2[i-2] + sticker[i]))
    print(dp2)
    return max(dp1[len(dp1)-1], dp2[len(dp2)-1])
