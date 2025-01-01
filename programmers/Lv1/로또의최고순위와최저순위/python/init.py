def solution(lottos, win_nums):
    answer = []
    numberRange = list(range(1, 46))
    matchingCountBest = 0
    matchingCountWorst = 0
    countZero = 0
    
    for lottoNum in lottos:
        print(lottoNum)
        if lottoNum in win_nums:
            win_nums.remove(lottoNum)
            numberRange.remove(lottoNum)
            matchingCountBest += 1
            matchingCountWorst += 1
        else:
            if lottoNum == 0:
                countZero += 1
            else:
                numberRange.remove(lottoNum)

    for i in range(countZero):
        for j in numberRange:
            if j in win_nums:
                win_nums.remove(j)
                numberRange.remove(j)
                matchingCountBest += 1
                break
                
    if matchingCountBest == 6:
        answer.append(1)
    elif matchingCountBest == 5:
        answer.append(2)
    elif matchingCountBest == 4:
        answer.append(3)
    elif matchingCountBest == 3:
        answer.append(4)
    elif matchingCountBest == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    if matchingCountWorst == 6:
        answer.append(1)
    elif matchingCountWorst == 5:
        answer.append(2)
    elif matchingCountWorst == 4:
        answer.append(3)
    elif matchingCountWorst == 3:
        answer.append(4)
    elif matchingCountWorst == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer


# dev
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt0 + ans], rank[ans]