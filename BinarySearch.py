def BinarySearch(arr, target):
   low, high = 0, len(arr) - 1

   while low <= high:
       mid = (low + high) // 2

       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           low = mid + 1
       else:
           high = mid - 1

   return -1

arr = [4,5,2,8,7,6,1,9,20]
target = 4
print(BinarySearch(arr, target))