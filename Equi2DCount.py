def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    B = transpose(A)
    a = []
    b = []
    for i in A:
        a.append(sum(i))
    for i in B:
        b.append(sum(i))
    count_a = 0
    count_b = 0
    for i in range(len(a)):
        if sum(a[:i])==sum(a[i+1:]):
            count_a += 1
    for i in range(len(b)):
        if sum(b[:i])==sum(b[i+1:]):
            count_b += 1
    return count_a * count_b
    pass

def transpose(n):
    return [list(row) for row in zip(*n)]

if __name__ == "__main__":
    q = [[int(i) for i in j.split(',')] for j in input().split('_')]
    print(solution(q))

