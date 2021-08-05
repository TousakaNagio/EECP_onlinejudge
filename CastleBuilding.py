def solution(A):
    if(len(set(A))==1):
        return 1
    count = 0
    A.append(-1)
    A.append(-1)
    i = 0
    while(A[i+1]!=-1):
        while(A[i]==A[i+1]):
            A.pop(i+1)
        i += 1
    A.pop(-1)
    A.pop(-1)
    for i in range(1,len(A)-1):
        if (A[i-1]<A[i] and A[i]>A[i+1]) or (A[i-1]>A[i] and A[i]<A[i+1]):
            count += 1   
    return count + 2
            
    pass

if __name__ == "__main__":
    q = [int(n) for n in input().split(',')]
    print(solution(q))

