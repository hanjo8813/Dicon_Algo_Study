from itertools import permutations
def solution(numbers):
    answer=0


    temp = []
    for x in range(1, len(numbers) + 1):
        c = list(set(list(permutations(numbers, x))))

        for i in c:
            temp.append(int("".join(list(map(str, i)))))

    temp = list(set(temp))

    for i in temp:
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break


        if (i>1 and cnt==0):
            answer += 1
    return answer
print(solution("17"))