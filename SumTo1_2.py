import math
def solution(X, Y):
    n = len(X)
    count = 0
    tot = {}
    for i in range(n):
        g = math.gcd(X[i], Y[i])
        X[i] = X[i] // g
        Y[i] = Y[i] // g
    for i in range(n):
        temp = (X[i], Y[i])
        complement = (Y[i] - X[i], Y[i])
        if complement in tot:
            count += tot[complement]
        if temp not in tot:
            tot[temp] = 1
        else:
            tot[temp] += 1
    return count % 1000000007

if __name__ == "__main__":
    X = [ int(value) for value in input().split(",") if len(value) > 0 ]
    Y = [ int(value) for value in input().split(",") if len(value) > 0 ]
    print(solution(X,Y))