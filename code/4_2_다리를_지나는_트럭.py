def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait=[0]*bridge_length

    while len(wait)!=0:
        answer+=1
        wait.pop(0)
        if truck_weights:
            if (sum(wait)+truck_weights[0]<=weight):
                wait.append(truck_weights.pop(0))
            else:
                wait.append(0)



    return answer
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))