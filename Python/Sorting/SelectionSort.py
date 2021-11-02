#working
#in slection sort two arrays will be maintained one is input array which is un sorted and other is for stroing the result which is sorted 
#in every iteration the minimum number from the unsorted array is stored in the beginning of the sorted or result array and minimum number in unsorted array is replaced with INF
# atlast the res array contain all the element from the input array in a sorted manner.
#this is an naive implementation which is not optimized
#time complexity : O(n^2)

def selectionSort1(arr):
  res = [0 for i in range(len(arr))]
  for index1 in range(len(arr)):
    minIndex=0
    for index2 in range(1,len(arr)):
      if(arr[index2] < arr[minIndex]):
        minIndex = index2
    res[index1] = arr[minIndex]
    arr[minIndex] = float('inf')
  return res  




#the above algorithm can be optimized to sort inplace instead using addition array for storing the sorted numbers
#the optimization can be done simply swapping the element at index1 with element at minIndex


def selectionSort2(arr):
  for index1 in range(len(arr)):
    #every iteration minIndex is set to value of index1 as the all the elements before index1 is already sorted in previous iterations
    minIndex=index1
    #in evry iteration the index2 has to should be in the range index1 to N as the elements before index1 is already sorted in previous iterations
    for index2 in range(index1+1,len(arr)):
      if(arr[index2] < arr[minIndex]):
        minIndex = index2
    #simply swapping the index1 element with minIndex element as minIndex element is the smallest of all and that should occur first
    arr[index1],arr[minIndex] = arr[minIndex],arr[index1]
  return arr  


print(selectionSort2([10,9,32,53,12,34]))

#time complexity is same as O(N^2)
