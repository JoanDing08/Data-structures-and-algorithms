#Implement queue using two stacks

class stack():
  def __init__(self,n):
    self.stack=[]
    self.n=n
  def push(self,item):
    if len(self.stack)<self.n:
      self.stack.append(item)
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

class queue():
  def __init__(self,n):
    self.s1=stack(n)
    self.s2=stack(n)
    self.size=n
    self.space=n

  def enqueue(self,item):
    if self.space==0:
      print("queue overflow")
    else:
      self.s1.push(item)
      self.space-=1

  def dequeue(self):
    if self.space==self.size:
      print("queue underflow")
    else:
      while self.s1.stack:
        self.s2.stack.append(self.s1.stack.pop())
      self.s2.pop()
      while self.s2.stack:
        self.s1.stack.append(self.s2.stack.pop())
      self.space+=1

  def getFront(self):
    print(self.s1.stack[0])

  def getEnd(self):
    print(self.s1.stack[-1])

  def Size(self):
    print(len(self.s1.stack))

  def display(self):
    print(self.s1.stack)


q=queue(8)

q.enqueue(5)
q.enqueue(19)
q.display()

q.enqueue(3)
q.enqueue(24)
q.enqueue(11)
q.display()

q.dequeue()
q.display()

q.getEnd()

q.getFront()

q.Size()
