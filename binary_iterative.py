def binary_iterated(arr,target):

  low=0
  high=len(arr)-1
  mid=(low+high)//2

  while low<=high:
    if arr[mid]==target:
      return arr[mid]
    elif arr[mid]<target:
      low=mid+1
    else:
      high=mid-1
  return -1


if __name__=="__main__":
  list=[1,2,4,16,20,25,33,64]
  target1=64
  target2=2

  index1=binary_iterated(list,target1)
  index2=binary_iterated(list,target2)

  print(f"Target: {target1}, Found: {index1}")
  print(f"Target: {target2}, Found: {index2}")
