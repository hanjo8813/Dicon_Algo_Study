'''  시간초과됨  모든 조합생성하고 최댓값 찾기 ㅎㅎ
from itertools import permutations
def solution(numbers):
    answer = ''

    temp=[]
    c=list(list(permutations(numbers,len(numbers))))

    for i in c:
       temp.append(int("".join(list(map(str,i)))))

    answer=str(max(temp))

    return answer
'''

def solution(numbers):
    answer=''
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x: x*3,reverse=True) # 주어지는 문자열의 최댓값이 1000이기 떄문에 3자리로 맞춰주기위해 문자열 *3으로 한후 문자열의 내림차순으로 정렬
    answer=str(int(''.join(numbers)))
    return answer
numbers = [3,5,34,39,30]

print(solution(numbers))
print(numbers)