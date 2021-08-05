import random

def solution(A, B):
    a = sum(A)/2
    b = sum(B)/2
    if(a == b):
        count = 0
        total = 0
        c = 0
        l = 0
        for i in range(1,len(A)):
            total += A[i-1]
            if total==a:
                c = c + sum(B[l:i])
                l = i
                if(c==total):
                    count += 1
        return count
    return 0
    pass

if __name__ == "__main__":
    A = [ int(value) for value in input("").split(",") ]
    B = [ int(value) for value in input("").split(",") ] 
    print(solution(A, B))

