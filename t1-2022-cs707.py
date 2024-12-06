class Stack:
    def __init__(self, size):
        self.li = [None] * size
        self.top = -1                             #task1
        
    def push(self, value):
        self.top += 1
        self.li[self.top] = value
        
    def pop(self):
        if self.empty():  
            return None  
        val = self.li[self.top]
        self.top -= 1
        return val
    
    def empty(self):
        return self.top == -1
    
    def stacksize(self):
        return self.top + 1


s = Stack(5)
s.push(3)
s.push(2)
s.push(1)
print("the first popped item",s.pop())  

for i in range(5):
    if not s.empty():
        x = s.pop() 
        print("after popped items:", x)
        a = s.stacksize()
        print("size of stack", a)
    else:
        print("wrong")


        