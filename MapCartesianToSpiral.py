import math
def solution(X, Y):
    if X==0 and Y==0:
        return 0
    x = 0
    y = 0
    count = 0
    if X==Y and X<0:
        count = 2*to_it(X)
        return count
    elif X<0 and abs(X)>=abs(Y):
        x = X
        y = x
        count = 2*to_it(x)
        a = -x*2
        for i in range(a):
            y += 1
            count += 1
            if x==X and y==Y:
                return count
    elif abs(Y)<abs(X):
        x = -(abs(X)-1)
        y = x
        count = to_it(x)
    elif abs(Y)>=abs(X):
        y = -(abs(Y)-1)
        x = y
        count = to_it(y)
    
    count = count * 2
    a = -x*2+1
    b = -x*2+2
    for i in range(a):
        y += 1
        count += 1
        if x==X and y==Y:
            return count
    for i in range(a):
        x += 1
        count += 1
        if x==X and y==Y:
            return count
    for i in range(b):
        y -= 1
        count += 1
        if x==X and y==Y:
            return count
    for i in range(b):
        x -= 1
        count += 1
        if x==X and y==Y:
            return count
    return count
    pass

def to_it(A):
    A = (-A)*2
    return int((A+1)*A/2)
    pass

if __name__ == "__main__":
    q = (int(input()), int(input()))
    print(solution(*q))
