def factorial(n):
  if n==0:
    return 1
  elif n==1:
    return 1
  elif n<0:
    return "Please enter a valid number."
  else:
    return n*(factorial(n-1))

for i in range(5):
  print(factorial(i))
