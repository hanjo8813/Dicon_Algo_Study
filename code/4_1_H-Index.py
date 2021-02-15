def solution(citations):
    answer = 0
    n=len(citations)
    citations.sort(reverse=True)

    for i in citations:
        if citations.index(i)+1<=i:
            answer=citations.index(i)+1
        else:
            break

    return answer

citations=[3,0,6,1,5]
print(solution(citations))