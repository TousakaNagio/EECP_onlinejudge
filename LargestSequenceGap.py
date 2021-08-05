def solution(A):
    # write your code in Python 3.6
    # you only need to modify this function
    quicksort(A,0,len(A)-1)
    max = 0
    for i in range(len(A)-1):
        if(max < (A[i+1]-A[i])):
            max = A[i+1] - A[i]
    if ((max)%2==1):
        return int((max-1)//2)
    else :
        return int(max//2)
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
    q = [int(i) for i in input().split(',')]
    print(solution(q))