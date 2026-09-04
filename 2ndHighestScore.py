def secondhighestScorefromlist(scores):

    scores=list(set(scores))  # it will remove the duplicates in the list
    scores.sort()
    print(scores)
    return scores[-2]

n=int(input())
scores = list(map(int, input().split()))
print(scores)
print(secondhighestScorefromlist(scores))


