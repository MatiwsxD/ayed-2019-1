from tkinter import *
from aplicacion import *
from tkinter import messagebox

class Screen:
    def __init__(self,a,b):
        self.frame=Tk()
        self.frame.title("Pacman")
        self.next=False
        self.pac=None
        self.lbl=[[None for x in range(b)] for a in range(a)]
        self.creeMapa(a,b)
        self.imagenes()
        self.dibuje()
        self.frame.mainloop()

    def solucion(self):
        if(self.pac!=None):
            self.ruta=self.pac.soluciona(self.mapa.getMap())
            self.next=True
            self.pos=0
            self.dibuje()
    
    def imagenes(self):
        self.barrera=PhotoImage(file="barrera.png")
        self.fantasma=PhotoImage(file="ghost.png")
        self.pacman=PhotoImage(file="pac.png")
        self.galleta=PhotoImage(file="galleta.png")
        self.galletac=PhotoImage(file="galletac.png")
        self.grafic=self.mapa.getMap()
        self.fantasma=self.fantasma.subsample(self.reduzca,self.reduzca)
        self.pacman=self.pacman.subsample(self.reduzca,self.reduzca)
        self.barrera=self.barrera.subsample(self.reduzca,self.reduzca)
        self.galleta=self.galleta.subsample(self.reduzca,self.reduzca)
        self.galletac=self.galletac.subsample(self.reduzca,self.reduzca)

    def botones(self):
        self.grafic=self.mapa.getMap()
        self.cor=Entry(self.frame)
        self.cor.grid(row=0,column=len(self.grafic[0]))
        self.cor2=Entry(self.frame)
        self.cor2.grid(row=1,column=len(self.grafic[0]))
        self.cor3=Entry(self.frame)
        self.cor3.grid(row=2,column=len(self.grafic[0]))
        bfantasma=Button(self.frame,text="Agregar fantasma",command= lambda:self.agregueFantasma(self.cor.get())).grid(row=0,column=len(self.grafic[0])+1)
        bpacman=Button(self.frame,text="Crear pacman",command= lambda:self.creePac(self.cor2.get())).grid(row=1,column=len(self.grafic[0])+1)
        bira=Button(self.frame,text="Ir a",command= lambda:self.irA(self.cor3.get())).grid(row=2,column=len(self.grafic[0])+1)
        bsolu=Button(self.frame,text="Soluciona",command= self.solucion).grid(row=3,column=len(self.grafic[0])+1)

    #n^2
    def dibuje(self):
        wid=self.frame.grid_slaves()
        for l in wid:
            l.destroy()
        self.grafic=self.mapa.getMap()
        for i in range(len(self.grafic)):
            for j in range(len(self.grafic[i])):
                if(self.grafic[i][j]=='-'):
                    img=self.barrera
                elif(self.grafic[i][j]=='F'):
                    img=self.fantasma
                elif(self.grafic[i][j]=='.'):
                    img=self.galleta
                else:
                    img=self.galletac
                self.lbl[i][j]=Label(self.frame,image=img).grid(row=i,column=j)
        if(self.pac!=None):
            pi=self.pac.getI()
            pj=self.pac.getJ()
            img=self.pacman
            self.lbl[pi][pj]=Label(self.frame,image=img).grid(row=pi,column=pj)
        labl=Label(self.frame,text=str(self.mapa.getScore())).grid(row=4,column=len(self.grafic[0])+1)
        labo=Label(self.frame,text="Score").grid(row=4,column=len(self.grafic[0]))
        if(self.next):
            bnext=Button(self.frame,text="Next",command= self.nextM).grid(row=len(self.grafic)-1,column=len(self.grafic[0])+1)
        self.botones()

    def creeMapa(self,n,m):
        self.reduzca=max(n,m)
        self.mapa=Map(n,m)

    def agregueFantasma(self,c):
        try:
            i,j=map(int,c.strip().split(","))
            self.mapa.agregaFantasma(i,j)
            self.dibuje()
        except(ValueError):
            messagebox.showerror("Error","Formato Incorrecto")

    def creePac(self,c):
        try:
            i,j=map(int,c.strip().split(","))
            if(self.grafic[i][j]!='-' and self.grafic[i][j]!='F'):
                self.pac=Pac(i,j)
            else:
                messagebox.showerror("Error","Obstaculo en esa ubicacion")
            self.dibuje()
        except(ValueError):
            messagebox.showerror("Error","Formato Incorrecto")

    def irA(self,c):
        if(self.pac!=None):
            try:
                i,j=map(int,c.strip().split(","))
                if(self.grafic[i][j]!='-' and self.grafic[i][j]!='F'):
                    self.ruta=self.pac.irAlPunto(i,j,self.mapa.getMap())
                    self.next=True
                    self.pos=0
                    self.dibuje()
                else:
                    messagebox.showerror("Error","Obstaculo en esa ubicacion")
            except(ValueError):
                messagebox.showerror("Error","Formato Incorrecto")

    def nextM(self):
        n=self.ruta[self.pos] #Tupla de la posicion siguiente
        ai=self.pac.getI()
        aj=self.pac.getJ()
        self.pac.posicion(n[0],n[1])
        self.mapa.comerGalleta(ai,aj)
        if(self.pos==len(self.ruta)-1):
            self.next=False
        self.pos+=1
        self.dibuje()



def main():
    a=int(input("Ingrese alto: "))
    b=int(input("Ingrese ancho: "))
    s=Screen(a,b)
    
main()

