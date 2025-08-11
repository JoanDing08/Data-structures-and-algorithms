open=["[","{","("]
closed=["]","}",")"]

def check(Str):
  stack=[]
  for i in Str:
    if i in open:
      stack.append(i)
    elif i in closed:
      pos=closed.index(i)
      if len(stack)>0 and open[pos]==stack[len(stack)-1]:
        stack.pop()
      else:
        return "unbalanced"
  if len(stack)==0:
    return "balanced"
  else:
    return "unbalanced"

print(check("[hello]"))
print(check("(1))"))
