def solution(answers):
    answer=[]
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(0, len(answers)):
        if (a1[i % 5] == answers[i]):
            cnt1 = cnt1 + 1
        if (a2[i % 8] == answers[i]):
            cnt2 = cnt2 + 1
        if (a3[i % 10] == answers[i]):
            cnt3 = cnt3 + 1

    if (cnt1 >= cnt2 and cnt1 >= cnt3):
        answer.append(1);
    if (cnt2 >= cnt1 and cnt2 >= cnt3):
        answer.append(2);
    if (cnt3 >= cnt1 and cnt3 >= cnt2):
        answer.append(3);
    return answer

answers=[1,3,2,4,2]
print(solution(answers))