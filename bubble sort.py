def bubbleSort(arr):
  n=len(arr)
  for i in range(n):
    swapped=False
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        swapped=True
    if not swapped:
      break
  return arr

array=[5,43,8,19,20,0,4]

print(bubbleSort(array))
