def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    max = 0
    for i in range(1,len(A)-1):
        left = 0
        right = 0
        k = i
        while(A[k+1]>=A[i]):
            k += 1
            right += 1
            if k == len(A)-1:
                break
        k = i
        while(A[k-1]>=A[i]):
            k -= 1
            left += 1
            if k == 0:
                break
        if A[i]*(right+left+1) > max:
            max = A[i]*(right+left+1)
    i = 0
    right = 0
    while(A[i+1]>=A[0]):
        i += 1
        right += 1
        if i == len(A)-1:
            break
    if A[0]*(right+1)>max:
        max = A[0]*(right+1)

    i = len(A)-1
    left = 0
    while(A[i-1]>=A[-1]):
        i -= 1
        left += 1
        if i == 0:
            break
    if A[-1]*(left+1)>max:
        max = A[-1]*(left+1)
    return max
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))

