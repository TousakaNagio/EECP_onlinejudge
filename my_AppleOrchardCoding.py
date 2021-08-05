def solution(A, K, L):
    if K+L>len(A):
        return -1
    total_1,total_2 = 0,0
    if find_max(A,K) >= find_max(A,L):
        total,T = find_max(A,K)
        a = A[:T[0]]
        b = A[T[-1]+1:]
        if len(a)>L:
            total_1,T1 = find_max(a,L)
        if len(b)>L:
            total_2,T2 = find_max(b,L)
        total = total + max(total_1,total_2)
    elif find_max(A,K) < find_max(A,L):
        total,T = find_max(A,L)
        a = A[:T[0]]
        b = A[T[-1]+1:]
        if len(a)>K:
            total_1,T1 = find_max(a,K)
        if len(b)>K:
            total_2,T2 = find_max(b,K)
        total = total + max(total_1,total_2)
    return total
    pass


def find_max(a,x):
    m = sum(a[:x])
    max_ = m
    L = []
    for i in range(x,len(a)):
        m = m + a[i] - a[i-x]
        if m > max_:
            max_ = m
            for s in range(i-x+1,i+1):
                L.append(s)
    return max_,L
    pass
 
if __name__ == "__main__":
    q = ([int(i) for i in input().split(',')], int(input()), int(input()))
    print(solution(*q))