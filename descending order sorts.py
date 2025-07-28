#Implement the bubble sort and insertion sort to sort the elements in descending order.

def bubbleSort(arr):
  n=len(arr)
  for i in range(n):
    swapped=False
    for j in range(n-i-1):
      if arr[j]<arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped=True
    if not swapped:
      break
  return arr

def insertionSort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key>arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr

array=[5,43,8,19,20,0,4]

print(bubbleSort(array))
print(insertionSort(array))