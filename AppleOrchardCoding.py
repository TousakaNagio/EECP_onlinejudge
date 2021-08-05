def solution(A, K, L):
    if K+L > len(A):
        return -1
    if K >= L :
        big = K
        small = L
    if K < L :
        big = L
        small = K    
    sum_A = []
    sum_B = []
    for n in range(len(A)-bi+1):
        sum_A.append([n,sum(A[n:n+big])])
    for n in range(len(A)-small+1):
        sum_B.append([n,sum(A[n:n+small])])
    result = 0
    local_sum = 0
    for i in sum_A:
        for j in sum_B:
            if  j[0] - i[0] >= 0 and j[0] - i[0] < big or i[0] - j[0] >=0 and i[0] - j[0] < small:
                continue
            local_sum = i[1] + j[1]
            if local_sum > result:
                result = local_sum
    return result 

if __name__ == "__main__":
    q = ([int(i) for i in input().split(',')], int(input()), int(input()))
    print(solution(*q))