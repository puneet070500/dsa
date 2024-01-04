def LinearSearch(arr,target):
    if not arr:
        return -1 
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5,1,4,8,2,3,0,9,6]
target = 8
c = LinearSearch(arr,target)
if c != -1:
    print(f"value found in {c} index")
else:
    print("Value not found")