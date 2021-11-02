#working 
# in the first pass the largest elemet in the arr will be moved to the end
# in the second pass the second largest elemet will be moved to its correct location
# like wise all the elements are moved ultil the whole arr is sorted
def bubbleSort1(arr):
  for index1 in range(len(arr)):
    for index2 in range(len(arr)):
      if(arr[index1] < arr[index2]):
        arr[index1],arr[index2] = arr[index2],arr[index1]
  return arr      


#below is the optimized vertion of bubble sort
def bubbleSort(arr):
  for index1 in range(len(arr)):
    #swapped variable is a optimizing term
    swapped =False  
    for index2 in range(len(arr)):
      if(arr[index1] < arr[index2]):
        swapped = True
        arr[index1],arr[index2] = arr[index2],arr[index1]
    if(swapped == False):
      return arr    
  return arr      
print(bubbleSort1([10,9,32,53,12,34]))  


# the optimization is done by adding swapped variable
# everytime while completing one pass this swapped variable is checked and if swapped is false thenn no swapping is done and the array is already sorted.
# this prevent from going for another pass which is not needed as the arr is already sorted          
