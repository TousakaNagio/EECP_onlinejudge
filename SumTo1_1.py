def solution(X, Y):
    Z = []
    count = 0
    for i in range(len(X)):
        if X[i]>=Y[i]:
            X.pop(i)
            Y.pop(i)

    for i in range(len(X)):
        Z.append(gcd(X[i],Y[i]))

    for i in range(len(X)):
        X[i] = X[i]//Z[i]
        Y[i] = Y[i]//Z[i]
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            if Y[i]==Y[j]:
                if X[i]+X[j]==Y[i]:
                    count += 1 
    
    return count
    pass

def gcd(a,b):
    while b:
        r = a%b
        a = b
        b = r
    return a

if __name__ == "__main__":
    X = [ int(value) for value in input().split(",") if len(value) > 0 ]
    Y = [ int(value) for value in input().split(",") if len(value) > 0 ]
    print(solution(X,Y))