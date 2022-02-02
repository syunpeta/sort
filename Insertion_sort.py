def insertion_sort(a):
    N=len(a)
    for i in range(N):
        v=a[i]
        j=i-1

        while j>=0 and a[j] >v:
            a[j+1] = a[j]
            j-=1
        a[j+1] =v
    

    return a
        
        
if __name__ == '__main__':

    #list
    a=list(map(int,input().split()))

    sorted_a =insertion_sort(a)

    print(sorted_a)