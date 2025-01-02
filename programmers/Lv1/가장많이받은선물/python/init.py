# 2022 KAKAO BLIND RECRUITMENT
def solution(id_list, report, k):
    answer = []
    report = set(report)
    userReports = {user: [] for user in id_list}
    reportCount = {user: 0 for user in id_list} 

    for r in report:
        reporter, reported = r.split()
        userReports[reporter].append(reported)
        reportCount[reported] += 1

    suspensionList = {user for user, count in reportCount.items() if count >= k}

    for user in id_list:
        result = len(set(userReports[user]) & suspensionList)
        answer.append(result)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))