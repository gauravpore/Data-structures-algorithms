def search(arr,x):
    #func for linear Search
    for i in range(0,len(arr)):
        if arr[i]==x:
            print("Element found at index: ",i)



def binary_search(arr,l,r,x):
    #func for binary_search
    if r>=l:
        mid = l + (r-2)//2
        if arr[mid]==x:
            return 'Element found at index: ',mid
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else :
            return binary_search(arr,mid+1,r,x)
    else:
        return "Not Found"

arr = [12,13,23,21,45]
print (binary_search(arr,0,len(arr),21))
x=13
search(arr,x)


