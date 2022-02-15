"""
https://programmers.co.kr/learn/courses/30/lessons/92334

"""

def solution(id_list, report, k):
    answer = []
    # dict 생성

    report_dict = {}

    # report : 내가 신고한 사람
    # report_num : 내가 신고 당한 횟수
    for id_name in id_list:
        report_dict[id_name] = {

            "report" : [],
            "report_num" : 0,
            
        }

    # report를 돌면서 저장한다.
    # check_report_person에도 함께 저장을 진행한다.
    
    check_report_person = []

    for report_name in set(report):
        name, report_person_name = report_name.split()

        # 신고를 진행한다.
        # 1. 신고를 진행하는 사람에게 신고를 진행했다고 알려준다.
        report_dict[name]["report"].append(report_person_name)

        # 2. 신고를 당한사람에게는 report_person, report_num을 증가시켜존다.
        report_dict[report_person_name]["report_num"] += 1

        if report_dict[report_person_name]["report_num"] == k:
            check_report_person.append(report_person_name)

    for i in id_list:
        count = 0
        for j in check_report_person:
            if j in report_dict[i]["report"]:
                count +=1
        answer.append(count)


    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


print(solution(id_list, report, k))

