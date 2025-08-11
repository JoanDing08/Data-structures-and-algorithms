class stack():
  def __init__(self,n):
    self.stack=[]
    self.n=n
  def push(self,k):
    if len(self.stack)<self.n:
      self.stack.append(k)
    else:
      print("The stack is full")
  def pop(self):
    if len(self.stack)==0:
      print("The stack is empty")
    else:
      self.stack.pop(-1)
  def top(self):
    if len(self.stack)==0:
      print("The stack is empty")
    else:
      print(self.stack[-1])
  def size(self):
    print(len(self.stack))
  def display(self):
    if len(self.stack)!=0:
      print(self.stack)
    else:
      print("The stack is empty")

s=stack(10)
s.display()
s.push(6)
s.display()
s.push(3)
s.push(8)
s.display()
s.pop()
s.display()
