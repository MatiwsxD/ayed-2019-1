from collections import deque
from sys import stdin
import random
import math

class Nodo:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.nodos=[]

    def agregaNodo(self,nodo):
        self.nodos.append(nodo)

class Pac:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def posicion(self,i,j):
        self.i=i
        self.j=j

    def generaArbol(self):
        self.rute=[]
        vis=set()
        k=0
        j=0
        while(k<(len(self.tree)-1)):
            ver=self.tree[k]
            if(j==0):
                dis = math.sqrt((self.tree[k+1][0]-ver[0])**2)+((self.tree[k+1][1]-ver[1])**2)
                if(dis==1):
                    self.rute.append(self.tree[k+1])
                    k+=1
                else:
                    j=k+1
                    k-=1
            else:
                dis = math.sqrt((self.tree[j][0]-ver[0])**2)+((self.tree[j][1]-ver[1])**2)
                if(dis==1):
                    self.rute.append(self.tree[j])
                    vis.clear()
                    k=j
                    j=0
                    a=1
                else:
                    self.rute.append(self.rute[k])
                    k-=1
    
    def soluciona(self,mapa):
        self.tree=[]
        posI=(0,1,0,-1)
        posJ=(-1,0,1,0)
        vis=[[False for x in range(len(mapa[0]))] for a in range(len(mapa))]
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if(mapa[i][j]=='-' or mapa[i][j]=='F'):
                    vis[i][j]=True
        vis[self.i][self.j]=True
        stack=[(self.i,self.j)]
        while(stack):
            ver=stack.pop()
            self.tree.append(ver)
            for i in range(len(posI)):
                ai=ver[0]+posI[i]
                aj=ver[1]+posJ[i]
                if(not(vis[ai][aj])):
                    vis[ai][aj]=True
                    stack.append((ai,aj))
        #self.generaArbol()
        return self.tree
        

    def irAlPunto(self,di,dj,mapa): #Funciona con BFS para ir al punto di,dj en el mapa.mapa
        posI=(0,1,0,-1)
        posJ=(-1,0,1,0)
        vis=[[False for x in range(len(mapa[0]))] for a in range(len(mapa))]
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if(mapa[i][j]=='-' or mapa[i][j]=='F'):
                    vis[i][j]=True
        vis[self.i][self.j]=True
        cola=deque()
        cola.append([(self.i,self.j)])
        while(len(cola)!=0):
            for i in range(len(posI)):
                a=cola[0].copy()
                ai=cola[0][-1][0]+posI[i]
                aj=cola[0][-1][1]+posJ[i]
                a.append((ai,aj))
                if(ai==di and aj==dj and not(vis[ai][aj])):
                    return a
                elif(not(vis[ai][aj])):
                    vis[ai][aj]=True
                    cola.append(a)
            cola.popleft()
        return [(self.i,self.j)]

    def getI(self):
        return self.i

    def getJ(self):
        return self.j

 
class Map:
    #n hacia abajo
    #m hacia la derecha
    def __init__(self,n,m):
        self.generarMapa(n,m)
        self.puntaje=0
        
    def generarMapa(self,n,m):
        #Generado con un DFS
        self.matriz=[['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '-', '-', '-', '-', '-', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '-'], ['-', '-', '-', '.', '-', '.', '.', '.', '-', '-', '-', '.', '.', '.', '.', '.', '.', '.', '.', '.', '-', '.', '-', '.', '.', '.', '-', '.', '-', '-', '-'], ['-', '.', '.', '.', '-', '-', '-', '.', '-', '.', '-', '-', '-', '-', '.', '-', '.', '-', '-', '-', '-', '-', '-', '.', '-', '-', '-', '.', '.', '.', '-'], ['-', '.', '-', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '-', '.', '-'], ['-', '.', '-', '-', '-', '.', '-', '-', '-', '-', '-', '.', '-', '-', '-', '-', '-', '-', '-', '.', '-', '-', '-', '.', '-', '.', '-', '-', '-', '-', '-'], ['-', '.', '.', '.', '.', '.', '-', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '-', '.', '.', '.', '-', '.', '.', '.', '.', '.', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
        """posI=(0,1,0,-1)
        posJ=(-1,0,1,0)
        self.matriz=[[None for x in range(m)] for a in range(n)]
        for i in range(len(self.matriz)):
            self.matriz[i][0]='-'
            self.matriz[i][-1]='-'
        for i in range(len(self.matriz[0])):
            self.matriz[0][i]='-'
            self.matriz[-1][i]='-'
        a=random.randint(1,n-2)
        b=random.randint(1,m-2)
        pila=[(a,b)]
        while(pila):
            ver=pila.pop()
            self.matriz[ver[0]][ver[1]]='.'
            opciones=[]
            for i in range(len(posI)):
                if(ver[0]+posI[i]>0 and ver[0]+posI[i]<len(self.matriz)-1 and ver[0]+posJ[i]>0 and ver[0]+posI[i]<len(self.matriz[0])-1):
                    if(self.matriz[ver[0]+posI[i]][ver[1]+posJ[i]]==None and ((ver[0]+posI[i],ver[1]+posJ[i]) not in pila)):
                        opciones.append((ver[0]+posI[i],ver[1]+posJ[i]))
            t=True
            for i in opciones:
                if(t):
                    pila.append(i)
                else:
                    self.matriz[i[0]][i[1]]='-'
                t=random.choice([True,False])
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if(self.matriz[i][j]==None):
                    self.matriz[i][j]='-'"""

    def agregaFantasma(self,i,j):
        self.matriz[i][j]='F'

    def getMap(self):
        return self.matriz

    def comerGalleta(self,i,j):
        if(self.matriz[i][j]!='N'):
            self.matriz[i][j]='N'
            self.puntaje+=20

    def reset(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if(self.matriz[i][j]=='N'):
                    self.matriz[i][j]='.'
    def getScore(self):
        return self.puntaje
