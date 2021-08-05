known = {0:0,1:1}
def solution(N):
    # write your code in Python 3.6
    if N in known:
        return known[N]
    ans = solution(N-1) + solution(N-2)
    known[N] = ans
    return ans
    pass


if __name__ == "__main__":
    q = int(input())
    a = solution(q)%1000000
    print(a)
    """
    if(solution(q)>999999):
        a = str(solution(q))
        print(a[-6:])
    else:
        print(solution(q))
    """