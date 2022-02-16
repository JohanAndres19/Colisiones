import numpy as np
#---------------------------------
#------- Objeto-Nodo cabeza------

class Cabeza :
    def __init__(self,Posiscion,llave,nombre):
        self.posicion=Posiscion 
        self.llave=llave
        self.nombre=nombre
        self.siguiente=None

    def Agregar(self,clave,posicion,nombre):
        if self.siguiente==None:
            self.siguiente=Cabeza(posicion,clave,nombre)
        else:
            self.siguiente.Agregar(clave,posicion,nombre)    
        
    def Imprimir(self):
        if self.siguiente==None:
            return str(self.llave)
        else:
            return str(self.llave)+ '->' + self.siguiente.Imprimir()    

    def Get_llave(self):
        return self.llave

    def Set_siguiente(self,siguiente):
        self.siguiente=siguiente

    def Get_poscion(self):
        return self.posicion        
     
class colision:
    def __init__(self,diccionario,llaves):
       self.lista=[]
       self.diccionario=diccionario
       self.llaves=llaves
       self.primo=self.Siguente_primo(len(self.llaves))
    
    def Siguente_primo(self,n):   
        factor_primo = 2
        factores=[]
        aux=0    
        while len(factores)!=1:
            aux=n
            factores=[]
            while n>1:
                if n % factor_primo == 0:
                    n //= factor_primo   
                    factores.append(factor_primo)         
                else:  
                    factor_primo += 1       
            if len(factores)==1:
                factores=[0]
            else:
                aux+=1
                n=aux 
                factor_primo=2         
        else:
            return aux   

    def crear(self):
        self.lista.clear()
        for i in range(self.primo):
            self.lista.append(-1)

    def LLenar (self):
        pass

    def Set_primo(self,primo):
        self.primo=primo

    def Eliminar():
        pass

    def Get_Cabezalista(self):
        return self.lista
    
    def imprimir(self):
        matriz=[]
        fila=0
        for i in self.lista:
            if i!=-1 and i!=None: 
                palabra=str(i.Get_poscion())+','+i.Imprimir()
                aux=palabra.split(',')
                matriz.append(aux)
            else:
                matriz.append([str(fila),' '])
            fila+=1    
        return matriz
           
#------------------------------------------
#------- Algoritmos de colisiones---------

class Encadenamiento_lineal(colision):
    
    def __init__(self,diccionario,llaves):
        super().__init__(diccionario,llaves)
        self.coliciones=0

    def LLenar(self):
        self.crear()
        pila=[]
        for i in self.llaves: 
            if self.lista[i%self.primo]==-1:
                self.lista[i%self.primo]=Cabeza(i%self.primo,i,self.diccionario[i])
                pila.append(i%self.primo)
            else:
                pos=-1
                for j in range(len(self.lista)-1,-1,-1):
                    if j not in pila :
                        pos=j
                        pila.append(j)
                        break;
                self.lista[i%self.primo].Agregar(i,pos,self.diccionario[i])
                self.coliciones+=1
        self.cursor=Cursor(self.lista)                
        self.cursor.Crear_cursor(1)     

    def Eliminar(self,anterior,valor,numero):
        if valor.Get_llave()==numero:
            aux=None
            if anterior!=None:
                anterior.Set_siguiente(valor.siguiente)
                aux=anterior
            else:
                self.lista[self.lista.index(valor)]=valor.siguiente
            return valor.Get_poscion(),aux   
        else:
            return self.Eliminar(valor,valor.siguiente,numero)


class Doble_hash(colision):

    def __init__(self,diccionario,llaves) :
        super().__init__(diccionario,llaves)
        self.coliciones=0
        
    def LLenar(self):
        self.crear()
        for i in self.llaves:
            m= self.primo
            h= i%m
            fijo=1+i%(m-2)
            while self.lista[h]!=-1:
                if self.lista[h].Get_llave()!=i:
                    h=(h+fijo)%m
                else:
                    break    
            else:
                self.lista[h]=Cabeza(h,i,self.diccionario[i])
                self.coliciones+=1
        self.cursor=Cursor(self.lista)                
        self.cursor.Crear_cursor(2)     

    def Eliminar(self,valor):
            pos=-1
            for i in self.lista:
                if i!=-1 and i!=None: 
                    if i.Get_llave()==valor:
                        pos=self.lista.index(i)
                        self.lista[self.lista.index(i)]=-1       
                        break;
            return pos


class Prueba_cuadratica(colision):

    def __init__(self,diccionario,llaves):
        super().__init__(diccionario,llaves)
        self.coliciones=0

    def LLenar(self):
        self.crear()
        pruebas=(self.primo+1)//2
        for i in self.llaves:
            h= i % self.primo
            if self.lista[h]==-1:
                self.lista[h]=Cabeza(h,i,self.diccionario[i])
            else:
                j=1
                k=h
                while self.lista[h]!=-1 and j<pruebas:
                    h=(k+j*j)%self.primo
                    j+=1
                else:
                    self.lista[h]=Cabeza(h,i,self.diccionario[i])
                    self.coliciones+=1
        self.cursor=Cursor(self.lista)                
        self.cursor.Crear_cursor(3)     

    def Eliminar(self,valor):
        pos=-1
        for i in self.lista:
            if i!=-1 and i!=None: 
                if i.Get_llave() ==valor:
                    pos=self.lista.index(i)
                    self.lista[self.lista.index(i)]=-1       
        return pos
#--------------------------------------
#----------Objetocursor---------------

class Cursor:

    def __init__(self,cabezalista) :
        self.cursor=[]
        self.cabezalista=cabezalista
        self.disponible=[]

    def Crear_cursor(self,opcion):
        for i in range(2):
            aux=[]
            for j in range(len(self.cabezalista)):
                aux.append(0)
            self.cursor.append(aux) 
        
        if opcion ==1:
            for i in self.cabezalista:
                if i !=-1:
                    self.Crear_Encadamiento(i)
        elif opcion ==2:
            self.Crear_Doblehash()
        elif opcion ==3:
            self.Crear_Cuadratica()
    
    def Eliminar(self,opcion,valor):
        if opcion==1:
            self.Eliminar_Lineal(valor)
        elif opcion ==2:
            self.Eliminar_DobleHash(valor)
        elif opcion ==3:
            self.Eliminar_cuadratica(valor)
            

    def Eliminar_Lineal(self,valor):
        self.disponible.append(valor[0])
        self.cursor[0][valor[0]]='-'
        self.cursor[1][valor[0]]='-'
        if valor[1]!=None:
            self.cursor[1][valor[1].Get_poscion()-1]=valor[1].Get_llave()
            if valor[1].siguiente!=None:
                self.cursor[0][valor[1].Get_poscion()-1]=valor[1].siguiente.Get_poscion()
            else:    
                self.cursor[0][valor[1].Get_poscion()-1]=0
    
    def Eliminar_DobleHash(self,valor):
        self.disponible.append(valor)
        self.cursor[1][valor]='-'

    def Eliminar_cuadratica(self,valor):
        self.disponible.append(valor)
        self.cursor[0][valor]='-'
        self.cursor[1][valor]='-'


    def Crear_Encadamiento(self,valor):   
        if  valor!=None:
            if valor.siguiente!=None:
                self.cursor[0][valor.Get_poscion()]=valor.siguiente.Get_poscion()
                self.cursor[1][valor.Get_poscion()]=valor.Get_llave()        
            else:
                self.cursor[0][valor.Get_poscion()]=-1
                self.cursor[1][valor.Get_poscion()]=valor.Get_llave()
            self.Crear_Encadamiento(valor.siguiente)    
        

    def Crear_Doblehash(self):
        columna=0
        for i in self.cabezalista:
            if i !=-1 and i!=None:
                self.cursor[0][i.Get_poscion()]=i.Get_poscion()
                self.cursor[1][i.Get_poscion()]=i.Get_llave()
            else:
                self.cursor[0][columna]=columna
            columna+=1    

    def Crear_Cuadratica(self):  
        for i in self.cabezalista:
            if i !=-1:
                self.cursor[0][i.Get_poscion()]=i.Get_llave()
                self.cursor[1][i.Get_poscion()]=i.nombre

        
    def Get_cursor(self):
        return self.cursor

    def Get_disponible(self):
        return self.disponible[len(self.disponible)-1]


if __name__=='__main__':
    archivo=open('prueba.txt')
    entrada=archivo.readlines()
    entrada=entrada[3].split('|')
    llaves=entrada[0].split(',')
    nombres=entrada[1].split(',')
    llaves_sin_repetir=[]
    diccionario={}
    for i in range(len(llaves)):
        if int(llaves[i]) not in llaves_sin_repetir:
            llaves_sin_repetir.append(int(llaves[i]))
            diccionario[int(llaves[i])]=nombres[i]        
    prueba= Encadenamiento_lineal(diccionario,llaves_sin_repetir)
    prueba.LLenar()
    for i in prueba.imprimir():
        for j in i:
            print(j,end=" ")
        print()
    print(np.array(prueba.cursor.Get_cursor())) 
    print(prueba.coliciones)
    print("---------------------------------")
    print("preuba doble hash")
    prueba2= Doble_hash(diccionario,llaves_sin_repetir)
    prueba2.LLenar()
    prueba2.imprimir()
    print(np.array(prueba2.cursor.Get_cursor()))
    print("--------------------------------")
    print("prueba cudratica")
    prueba3= Prueba_cuadratica(diccionario,llaves_sin_repetir)
    prueba3.LLenar()
    prueba3.imprimir()
    print(np.array(prueba3.cursor.Get_cursor()))
