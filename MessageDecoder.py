def solution(S):
    # write your code in Python 3.6
    # you only need to modify this function
    A = list(S)
    A.reverse()
    count = 1
    last2 = 1
    for i in range(1,len(A)):
        if A[i]>=3:
            count = count*1
        elif A[i]==2:
            if A[i-1]>6:
                count = count * 1
            else:
                count = count + count
        elif A[i]==1:
            count = 2 * count
        else:
            
    return 
    pass

if __name__ == "__main__":
    q = input()
    print(solution(q))

