def solution(T):
    # write your code in Python 3.6
    
    k = find_index(T)
    if k == len(T)-1:
        return len(T)

    a = T[:k+1]
    b = T[k+1:]

    while max(a)>=min(b):
        a = a + b[:b.index(min(b))+1]
        b = b[b.index(min(b))+1:]

    return len(a)
    pass

def find_index(C):
    s = C.copy()
    c = min(s)
    s.reverse()
    k = s.index(c)
    return len(s)-k-1
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split('_')]
    print(solution(q))
