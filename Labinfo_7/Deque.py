
class Node():
    def __init__(self,x):
        self.val = x
        self.der = None
        self.izq = None
        

class DequeDoblemeneEncadenado():  
    def __init__(self):
        self.primero = None
        self.ultimo = None

        self.tamp = 0
        
    def append_right(self,x):
        nodo = Node(x)
        if self.ultimo == None:
            self.primero = self.ultimo = nodo
        else:
            self.ultimo.der = nodo
            nodo.izq = self.ultimo
            self.ultimo = nodo
        self.tamp += 1
        
    def append_left(self,x):
        nodo = Node(x)
        if self.primero == None:
            self.primero = self.ultimo = nodo
        else:
            self.primero.izq = nodo
            nodo.der = self.primero
            self.primero = nodo
        self.tamp += 1
        
    def pop_right(self):
        if self.ultimo == None:
            raise Exception("Imposible hacer pop, Deque vacío")
        x = self.ultimo.val
        if self.ultimo == self.primero:
            self.ultimo = self.primero = None
        else:
            penultimo = self.ultimo.izq
            penultimo.der = None
            self.ultimo = penultimo
        self.tamp -= 1
        return x
    
    def pop_left(self):
        if self.primero == None:
            raise Exception("Imposible hacer pop, Deque vacío, MI EDWIN <3")
        x = self.primero.val
        if self.ultimo == self.primero:
            self.ultimo = self.primero = None
        else:
            segundo = self.primero.der
            segundo.izq = None
            self.primero = segundo
        self.tamp -= 1
        return x
    
    def valores(self):
        nodo = self.primero 
        ans = []
        while nodo != None:
            ans.append(nodo.val)
            nodo = nodo.der
        return ans
    def __len__(self):
        return self.tamp
    def __str__(self):
        l = self.valores()
        return str(l)
        

q = DequeDoblemeneEncadenado()
print(q)
print()
q.append_right(3)
print(q)
print()
q.append_right(2)
print(q)
print()
q.append_right(5)
print(q)
print()
print(q.pop_right())
print()
print(q)
print()
q.append_left(7)
print(q)
print()
q.append_left(1)
print(q)
print()
q.append_left(0)
print(q)
print()
print(q.pop_right())
print()
print(q)
print()
print(q.pop_right())
print()
print(q)
print()
q.append_right(0)
print(q)
print()
print(q.pop_left())
print()
print(q)
print()
print()
print(len(q))
print()
print(q)
print()
print(q.pop_left())
print(q.pop_left())
print(q.pop_left())
print(q)
print(q.pop_left())


