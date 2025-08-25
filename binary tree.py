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

def search(root,key):
  if root.data==key:
    return root
  elif root.data>key and root.left is not None:
    return search(root.left,key)
  elif root.data<key and root.right is not None:
    return search(root.right,key)
  else:
    return -1
  
n=int(input("Enter the number of values you want: "))
root=None
for i in range(n):
  x=int(input("Enter a value: "))
  root=insert(root,x)

inorder(root)

key=int(input("Enter search key: "))
keynode=search(root,key)

if keynode==-1:
  print("Key not in tree")
else:
  print(f"Existing key: {keynode.data}")
