class treenode():
  def __init__(self,data):
    self.data=data
    self.leftnode=None
    self.rightnode=None
  
def inorder(root):
  if root.leftnode!=None:
    inorder(root.leftnode)
    print(f"inorder: {root.data}")
  if root.rightnode!=None:
    inorder(root.rightnode)
      
def preorder(root):
  print(f"preorder: {root.data}")
  if root.leftnode!=None:
    preorder(root.leftnode)
  if root.rightnode!=None:
    preorder(root.rightnode)
  
def postorder(root):
  if root.leftnode!=None:
    postorder(root.leftnode)
  if root.rightnode!=None:
    postorder(root.rightnode)
  print(f"postorder: {root.data}")

root=treenode(5)
root.leftnode=treenode(6)
root.leftnode.leftnode=treenode(7)
root.rightnode=treenode(3)

inorder(root)
preorder(root)
postorder(root)
