class Node():
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

def inorder(root):
  if root is not None:
    if root.left is not None:
      inorder(root.left)
    print(root.data)
    if root.right is not None:
      inorder(root.right)
  

def insert(root,data):
  if root==None:
    return Node(data)
  elif root.data>data:
    root.left=insert(root.left,data)
  elif root.data<data:
    root.right=insert(root.right,data)
  return root

def inorder_successor(root):
  current=root
  while current.left is not None:
    current=current.left
  return current

def delete(root,key):
  if root is None:
    return root
  if key<root.data:
    root.left=delete(root.left,key)
  elif key>root.data:
    root.right=delete(root.right,key)
  else:
    if root.left is None:
      temp=root.right
      root=None
      return temp
    elif root.right is None:
      temp=root.left
      root=None
      return temp
    else:
      temp=inorder_successor(root)
      print("hello",temp.data)
      t=root.data
      root.data=temp.data
      temp.data=t
      root.right=delete(root.right,temp.data)

n=int(input("enter the number of elements to put in a tree: "))
root=None
for i in range(n):
  x=int(input("enter the node value: "))
  root=insert(root,x)

inorder(root)
