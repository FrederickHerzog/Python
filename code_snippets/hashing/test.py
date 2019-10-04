#Frederick Herzog
from hash import *

def calcAll(s):
    for alg in algs:
        h = hash(s, alg)
        print(alg +': '+h)

s = 'hello'
calcAll(s)
