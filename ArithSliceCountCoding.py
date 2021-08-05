def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    count = 0
    for i in range(3,len(A)+1):
        for j in range(len(A)-i+1):
            if(is_arith(A[j:j+i])):
                count += 1
    return count
    pass

def is_arith(N):
    _len = len(N)
    for l in range(_len-2):
        if(N[l+1]-N[l] != N[l+2]-N[l+1]):
            return False
    return True          
pass

if __name__ == "__main__":
    q = [int(n) for n in input().split(',')]
    print(solution(q))

