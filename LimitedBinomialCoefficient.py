def solution(N, K):
    # write your code in Python 3.6
    if (0<=K and K<=N):
        if(N>=1000000000 and K>=1):
            return -1
        if((N-K)>K):
            ans = factorial_1(N,N-K)/factorial_1(K,1)
        else:
            ans = factorial_1(N,K)/factorial_1(N-K,1)
        
        if(ans>=1000000000):
            return -1
        return int(ans)
    return -1
    pass

def factorial_1(a,b):
    sum = 1
    while(a>b):
        sum = sum * a
        a -= 1
    return sum


if __name__ == "__main__":
    q = (int(input()), int(input()))
    print(solution(*q))

