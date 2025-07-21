def linear(arr,target):
  for i in range(len(arr)):
    if arr[i]==target:
      return i
  
  return "NOT AVAILABLE"


if __name__=="__main__":

  list1=[12,32,76,3,90,1,15]
  target1=32
  target2=1

  index1=linear(list1,target1)
  index2=linear(list1,target2)

  print(f"List: {list1}")
  print(f"The first item, {target1}, was found at {index1}")
  print(f"The second item, {target2}, was found at {index2}")

