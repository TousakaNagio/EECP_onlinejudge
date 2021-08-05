def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    b = []
    c = []
    for i in range(len(A)):
        if(A[i] in c):
            continue
        a = []
        a.append(A[i])
        c.append(A[i])
        k = A[i]
        while(A[k] != A[i]):
            a.append(A[k])
            c.append(A[k])
            k = A[k]
        if(len(a)>len(A)/2):
            return len(a)
        if len(a) not in b:
            b.append(len(a))
    print(c)
    return max(b)
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))

