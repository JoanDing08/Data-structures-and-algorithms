class queue():
  def __init__(self,n):
    self.queue=[None]*n
    self.front=0
    self.end=0
    self.size=n
    self.space=n
  def enqueue(self,item):
    if self.space==0:
      print("queue overflow")
    else:
      self.queue[self.end]=item
      self.end=(self.end+1)%self.size
      self.space-=1
  def dequeue(self):
    if self.space==self.size:
      print("queue underflow")
    else:
      self.queue[self.front]=None
      self.front=(self.front+1)%self.size
      self.space+=1
  def getFront(self):
    print(self.queue[self.front])
  def getEnd(self):
    print(self.queue[self.end])
  def Size(self):
    print(len(self.queue))
  def display(self):
    if len(self.queue)>0:
      print(self.queue)
    else:
      print("empty queue")

q=queue(6)

q.display
q.enqueue(5)
q.enqueue(8)
q.display()
q.enqueue(12)
q.display
q.dequeue()
q.display()
