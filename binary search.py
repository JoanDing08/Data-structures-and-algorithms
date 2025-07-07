import numpy as np

def binary_search(arr,target):
  left,right=0,len(arr)-1
  while left<=right:
    middle=(left+right)//2
    if arr[middle]==target:
      return middle
    elif arr[middle]<target:
      left=middle+1
    else:
      right=middle-1
  return "does not exist"

n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

target=int(input())

print(binary_search(n,target))
