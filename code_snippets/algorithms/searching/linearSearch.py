#Frederick Herzog

def lin_search(l, x):
  for i in range(len(l)):
    if l[i] == x:
      return "Target "+str(x)+" was found at index: "+str(i)
  return "Target "+str(x)+" not found.

a = [100, 20, 14, 7, 4, 12, 18, 24, 54, 99, 37, 8]
target = 24

lin_search(a, target)
