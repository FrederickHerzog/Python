#Fred Herzog

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

  
  gCd = gcd(1000, 86)
  print(gCd)
  
