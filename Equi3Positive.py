def solution(A):
    # write your code in Python 3.6
    if len(A)<5:
        return False
    left = 1
    right = len(A)-2
    total = sum(A)
    L = A[0]
    R = A[len(A)-1]
    C = 0
    while L < total/2.5:
        if L > R:
            R = R + A[right]
            right -= 1
        elif L < R:
            L = L + A[left]
            left += 1
        elif L == R:
            C = total - L - R - A[left] - A[right]
            if C == L:
                return True
            else:
                R = R + A[right]
                right -= 1
    return False
    pass

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))

