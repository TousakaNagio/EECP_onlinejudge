def solution(S):
    # write your code in Python 3.6
    a = list(S)
    while(a[0] == '0'):
        a = a[1:]
    count = 0
    for i in a:
        if(i=='1'):
            count += 1
    return len(a)+count-1
    pass

if __name__ == "__main__":
    print(solution(input("")))

