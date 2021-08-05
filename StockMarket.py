def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    max = 0
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if(A[j]-A[i]>max):
                max = A[j]-A[i]
    return max
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))

