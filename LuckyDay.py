def solution(N, K):
    count = 0
    while(N!=0):
        if(N%2==0 and K>0):
            N = N/2
            count += 1
            K -= 1
        elif(N%2==1 and K>0):
            N = N-1
            count += 1
            N = N/2
            count += 1
            K -= 1
        elif(K == 0):
            count = count + N
            N = 0
    if(K>0):
        return int(count-2)
    return int(count-1)
    pass

if __name__ == "__main__":
    q = (int(input()), int(input()))
    print(solution(*q))

