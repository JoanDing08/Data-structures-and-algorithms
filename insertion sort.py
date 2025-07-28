def insertionSort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=key
  return arr

array=[5,43,8,19,20,0,4]

print(insertionSort(array))
