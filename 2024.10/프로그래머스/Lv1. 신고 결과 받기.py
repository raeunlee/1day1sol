# def solution(id_list, report, k):
#     answer = []
    
#     # id_list 별로 고유 idx 부여
#     l = {}
#     idx = 0
#     for i in id_list:
#         l[i] = idx
#         idx += 1
    
#     # 신고당한 사람들 배열
#     bad = []
    
#     # 각 유저는 한 번에 한 명의 유저 신고
#     for i in l: # i는 신고할 유저 
#         tmp = [ ] # 신고당한 유저 담는 배열
#         for r in report:
#             a, b = r.split(" ")
#             if i == a and b not in tmp: # 신고자 배열에 없음 추가하기
#                 tmp.append(b)
#         bad.append(tmp)
#     print(bad)
    
#     #정지당한 횟수
#     blocks = {}
#     for b in bad:
#         for each in b:
#             if each in blocks:
#                 blocks[each] += 1
#             else:
#                 blocks[each] = 1
    
#     real_bad = []
#     for key, values in blocks.items():
#         if values >= 2:
#             real_bad.append(key)
    
#     print("진짜 신고당한 사람", real_bad)
    
#     for i in range(len(bad)):
#         count = 0
#         for b in bad[i]:
#             for real in real_bad:
#                 if b == real:
#                     count += 1
#         answer.append(count)
#     return answer

def solution(id_list, report, k):
    # 유저 별 고유 idx 딕셔너리 생성
    user_index = {user: i for i, user in enumerate(id_list)}
    
    # 중복 신고를 제거
    report_set = set(report)
    
    # 각 유저가 신고당한 횟수
    report_count = {}
    
    # 각 유저가 신고한 사람
    user_reports = {}
    
    # 모든 유저를 순회하며 초기화
    for user in id_list:
        report_count[user] = 0  # 신고 횟수는 0으로 초기화
        user_reports[user] = []  # 각 유저가 신고한 사람 목록 초기화
    
    # 신고 내역을 처리
    for r in report_set:
        reporter, reported = r.split()  # 신고자 신고당한 사람
        user_reports[reporter].append(reported)  # 신고자가 신고한 사람
        report_count[reported] += 1  # 신고당한 사람의 신고 횟수 증가
    
    # 정지 대상 유저 리스트 (k번 이상 신고당한 사람)
    banned_users = []
    for user, count in report_count.items():
        if count >= k:
            banned_users.append(user)  # 신고당한 횟수가 k 이상인 유저 추가
    
    # 각 유저가 받은 메일 수 계산
    answer = []
    for user in id_list:
        mail_count = 0
        # 해당 유저가 신고한 사람 중 정지된 사람이 있는지 확인
        for reported_user in user_reports[user]:
            if reported_user in banned_users:
                mail_count += 1
        answer.append(mail_count)  # 결과에 추가
    
    return answer
