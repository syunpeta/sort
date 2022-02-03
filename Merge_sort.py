from operator import le
from turtle import left


def MergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2

    #sort left
    a_left = MergeSort(a[:mid])
    #sort right
    a_right = MergeSort(a[mid:])

    #merge

    N = len(a_left + a_right)
    s =max(a_left + a_right)
    a_right.append(s)
    a_left.append(s)
    ans =[]
    while len(ans) <N:
        if(a_left[0] <= a_right[0]):
            ans.append(a_left.pop(0))
        else:
            ans.append(a_right.pop(0))
    return ans


    

    

if __name__ == '__main__':
    
    #list
    a=list(map(int,input().split()))

    ans =MergeSort(a)
    print(ans)

