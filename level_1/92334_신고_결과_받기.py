"""
신고 결과 받기
- 문제 : https://programmers.co.kr/learn/courses/30/lessons/92334
- 입출력 예
id_list	report	k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]
"""
import collections


def solution(id_list, report, k):
    dic_per_id = {id: {} for id in id_list}

    for r in report:
        splited_report = r.split(" ")
        from_user = splited_report[0]
        to_user = splited_report[1]

        from_user_dic = dic_per_id[from_user]
        if to_user not in from_user_dic:
            from_user_dic[to_user] = 1
            dic_per_id[from_user] = from_user_dic

    report_users = sum(
        [list(report_per_user.keys()) for report_per_user in dic_per_id.values()], []
    )  # list flatten
    report_user_dic = dict(collections.Counter(report_users))

    block_users = [
        user_id
        for user_id, report_count in report_user_dic.items()
        if report_count >= k
    ]

    answer = [
        len(
            [
                block_user
                for block_user in block_users
                if block_user in report_per_user.keys()
            ]
        )
        for report_per_user in dic_per_id.values()
    ]
    return answer


if __name__ == "__main__":
    input_data = (
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
    result = solution(*input_data)
    print(result)
