#kadane algorithm (largest sub-contiguous sum array)
def maxSubArraySum(a,size):
    curr_sum = 0
    max_sum = 0 #sum so far
    st=0 #start index
    end=0 #ending index
    poi=0 #pointer
    for i in range(0,size):
        curr_sum = curr_sum + a[i]
        if max_sum < curr_sum:
            st= poi
            end = i
            max_sum = curr_sum
        elif curr_sum<0:
            curr_sum = 0
            poi = i+1
    final_sum = 0
    for j in range(st,end+1):
        final_sum += a[j]
    return final_sum

arr = [-4,-3,2,4,6,-1,7,-2-3]
print (maxSubArraySum(arr,len(arr)))