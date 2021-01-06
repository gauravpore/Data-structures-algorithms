#program for selection sort
def selection_sort(A):
  for i in range (len(A)):
    min_idx = i #index of smallest element
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx = j
    A[i],A[min_idx] = A[min_idx],A[i]
  return A

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j] #swapping
                swapped = True
        if not swapped:
            break
    return A

def insertion_sort(A):
    for i in range(1,len(A)):
        current_ele = A[i]
        pos = i
        while current_ele<A[pos-1]and pos>0:
            A[pos] = A[pos-1]
            pos = pos -1
        A[pos] = current_ele
    return A




A = [23,45,11,22,54]
print (selection_sort(A))
print (bubble_sort(A))
print (insertion_sort(A))
