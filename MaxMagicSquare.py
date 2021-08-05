def solution(A):
    # write your code in Python 3.6
    row = len(A)
    col = len(A[0])
    min_ = min(row,col)
    for k in range(min_,0,-1):
        for i in range(col-k+1):
            for j in range(row-k+1):
                a = A[j:j+k]
                a = transpose(a)
                a = a[i:i+k]
                if is_equal(a):
                    return k
    return 0

def transpose(N):
    return [list(row) for row in zip(*N)]
    pass

def is_equal(N):
    n = transpose(N)
    a = []
    b = []
    for i in N:
        a.append(sum(i))
    if len(set(a))!=1:
        return False
    for i in n:
        b.append(sum(i))
    if len(set(b))!=1:
        return False
    if a[0] != b[0]:
        return False
    
    return True
    pass

if __name__ == "__main__":
    n_rows, n_cols = tuple([ int(v) for v in input().split(",") ])
    matrix = [ [ int(v) for v in input().split(",") ] for _ in range(n_rows) ]
    print(solution(matrix))

