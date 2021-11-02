#working
#is insertion sort the whole input array is devided into sorted part(left) and unsorted part(right).

#as a result the first iteration start from 1 to N

#in every iteration the the the first element in the unsorted array is moved to the sorted at correct position by comparing with all the elements in the sorted side.

#the element to be compared is stored in a separate varible key. now the every element in the sorted side is compared to the key and if the element is greater the key they moved opne position to right and it compares until it finds an element which less than key and insert it next to the lesser element


#time complexity: in case if the input array is sorted or partially sorted the time complexity of insertion sort will be O(N).

#in case if the array is reverse sorted then the time complexity will be O(N^2)

def InsertionSort(arr):
  for frwdIndex in range(1,len(arr)):
    key = arr[frwdIndex]
    backIndex = frwdIndex-1
    while(backIndex >=0 and arr[backIndex]>key):
      arr[backIndex+1] = arr[backIndex]
      backIndex-=1
    arr[backIndex+1] = key
  return arr    
print(InsertionSort([10,9,32,53,12,34]))