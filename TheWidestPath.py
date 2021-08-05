def solution(X, Y):
    # write your code in Python 3.6
    """
    for i in range(1,len(X)-1):
        for j in range(len(X)-i):
            if(X[j]>X[j+1]):
                X[j],X[j+1] = X[j+1],X[j]
    
    k = list(set(X))
    """
    quicksort(X,0,len(X)-1)
    max = 0
    for i in range(1,len(X)):
        if(max<(X[i]-X[i-1])):
            max = X[i]-X[i-1]

    return max
    pass

def quicksort(data,left,right):
    if left >=right:
        return
    i = left
    j= right
    key = data[left]

    while i != j:
        while data[j]>key and i<j:
            j -= 1
        while data[i] <= key and i<j:
            i += 1
        if i<j:
            data[i],data[j] = data[j],data[i]

    data[left] = data[i]
    data[i] = key

    quicksort(data,left,i-1)
    quicksort(data,i+1,right)

    pass

if __name__ == "__main__":
    X = [ int(v) for v in input().split(",") ]
    Y = [ int(v) for v in input().split(",") ]
    print(solution(X, Y))

