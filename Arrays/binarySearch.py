def binarySearch(arr,l,r,t):
    while(l<=r):
        m=(l+r)//2
        if(t<arr[m]):
            r=m-1
        elif(t>arr[m]):
            l=m+1
        else:
            return m
    return "not found"
x=binarySearch([1,4,6,8,10,12],0,5,0)
print(x)
