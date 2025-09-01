class Graph():
  def __init__(self,n):
    self.n=n
    self.adj=[[]*n for i in range(n)]
              
  def edge(self,x,y):
    self.adj[x-1].append(y-1)
    self.adj[y-1].append(x-1)
  
  def breadth_first(self,source):
    visited=[False]*self.n
    result=[]
    queue=[]
    queue.append(source)
    visited[source]=True
    while len(queue)>0:
      s=queue.pop(0)
      result.append(s)
      for node in self.adj[s]:
        if visited[node]==False:
          queue.append(node)
          visited[node]=True
    return result
  
g=Graph(6)

g.edge(1,4)
g.edge(2,3)
g.edge(6,5)

print(g.breadth_first(0))
