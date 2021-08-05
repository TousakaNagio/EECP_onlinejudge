def solution(A):
    if len(A) < 5 :
        return False
    B = A.copy()
    B.sort() 
    list_len = len(A)
    average_min = sum(B[:-2])//3   
    left  = A[0]
    right = A[list_len-1]
    l_key = 0
    r_key = list_len-1
    while left < average_min or A[l_key+1] == 0 :
        l_key += 1
        left += A[l_key]
    while right < average_min or A[r_key-1] == 0:
        r_key -= 1
        right += A[r_key]
    len_middle = r_key - l_key - 3
    if len_middle < 1:
        return False
    middle = sum(A[l_key+2:r_key-1]) 
    for n in range(len_middle):
        if left > right:
            r_key -= 1
            right += A[r_key]
            middle -= A[r_key-1]
            continue
        if left < right:
            l_key += 1
            left += A[l_key]
            middle -= A[l_key+1]
            continue
        if left > middle or right > middle :
            break
        elif left == middle == right:
            return True
    return False
             

if __name__ == "__main__":
    q = [int(i) for i in input().split(',')]
    print(solution(q))