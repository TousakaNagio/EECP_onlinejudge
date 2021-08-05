def solution(X, Y):
    count = 0
    A = []
    for i in range(len(Y)):
        if X[i]<Y[i]:
            A.append(X[i]/Y[i])
    B = list(set(A))
    B = sorted(B)
    C = []

    for i in B:
        C.append(A.count(i))

    left = 0
    right = len(B)-1
    while left<right:
        if B[left]+B[right] == 1:
            count = count + C[left]*C[right]
            left += 1
            right -= 1
            continue
        elif B[left]+B[right]>1:
            right -= 1
            continue
        else :
            left += 1
            continue
    
    if 0.5 in B:
        count = count + sum(C[B.index(0.5)])

    return int(count)
    pass

def sum(a):
    if a>=2:
        return a*(a-1)/2
    return 0
    pass

if __name__ == "__main__":
    X = [ int(value) for value in input().split(",") if len(value) > 0 ]
    Y = [ int(value) for value in input().split(",") if len(value) > 0 ]
    print(solution(X,Y))


