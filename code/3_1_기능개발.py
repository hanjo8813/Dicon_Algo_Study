import math #올림 사용하려고
def solution(progresses, speeds):
    answer=[]
    toDo=[] #남은 일수
    for i,j in zip(progresses,speeds):
        toDo.append(math.ceil((100-i)/j))

    print(toDo)
    cnt=0
    temp=toDo.pop(0) #첫번째 를 갖고 함
    for i in toDo:
        if temp<i:
            cnt+=1
            answer.append(cnt)
            temp=i
            cnt=0
            print(temp)
        else:
             cnt+=1

    cnt+=1 #마지막 원소에대한 값을 answer에 넣어주기위해ㄴ
    answer.append(cnt)
    return answer
progresses=[93,93,93]
speeds=[1,1,1]

print(solution(progresses,speeds))