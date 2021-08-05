def solution(A):
    B = []
    C = []
    for i in A:
        if i<0:
            B.append(i)
    for j in A:
        if j>0:
            C.append(j)
    C = sorted(C)
    C.reverse()
    for k in C:
        if -k in B:
            return k
    return 0

    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split('_')]
    print(solution(q))
