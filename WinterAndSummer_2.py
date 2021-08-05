def solution(T):
    n = len(T)
    _max, _min = [], []
    Max = T[0]
    for i in range(0, n):
        if T[i] > Max:
            Max = T[i]
        _max.append(Max)
    Min = T[n - 1]
    for i in range(n-1, -1, -1):
        if T[i] < Min:
            Min = T[i]
        _min.append(Min)
    _min.reverse()
    print(_max,_min)
    for j in range(n - 1):
        if _max[j] < _min[j + 1]:
            return j + 1
    return n

if __name__ == "__main__":
    q = [int(i) for i in input().split('_')]
    print(solution(q))