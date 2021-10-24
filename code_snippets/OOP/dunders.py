import inspect
from queue import Queue as q

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()

    
class Test:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f'Person({self.name})'
    
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument")

        else: self.name = self.name * x
    
    def __call__(self, y):
        print(y)
    
    def __len__(self):
        return len(self.name)








t = Test("***")
que = Queue()
print(t)
t * 5
print(t)
print(type(t))
print()
l = len(t)
print(l)
t(4)
print("---------------------")
que + 9
que + 7
print(que)
que + 4
que + 10
print(que)