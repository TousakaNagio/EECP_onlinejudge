def solution(N):
    # write your code in Python 3.6
    a ,b = 0 ,1
    for i in range(N):
        a,b = b,a+b
    return a
    pass


if __name__ == "__main__":
    q = int(input())
    k = str(solution(q))
    print(k[-6:])