#Make changes to merge sort to sort the numbers in descending order.

def merge(left,right):
  merged_list=[]
  l_index=0
  r_index=0
  while l_index<len(left) and r_index<len(right):
    if left[l_index]>=right[r_index]:
      merged_list.append(left[l_index])
      l_index+=1
    else:
      merged_list.append(right[r_index])
      r_index+=1
  while l_index<len(left):
    merged_list.append(left[l_index])
    l_index+=1
  while r_index<len(right):
    merged_list.append(right[r_index])
    r_index+=1
  return merged_list

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr)//2
  left_half=arr[:mid]
  right_half=arr[mid:]
  left_sorted=merge_sort(left_half)
  right_sorted=merge_sort(right_half)
  return merge(left_sorted,right_sorted)

array=[5,86,13,2,44,90,54,21,36]

print(f"Unsorted: {array}\nSorted (descending): {merge_sort(array)}")
