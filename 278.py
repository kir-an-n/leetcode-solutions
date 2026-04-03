#Find the index where target would be inserted in sorted array

def search_insert(nums,target):
    left=0
    right=len(nums)-1

    while left <= right:
          mid=(left+right) //2

          if mid ==target:
               return mid
          
          elif mid < target:
               left =mid+1

          else: right =mid-1

    return left 

print(search_insert([1,2,4,5],3))