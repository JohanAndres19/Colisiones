from cProfile import label
import sys
from PyQt5.QtGui import QTextOption 
from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from qt_for_python.uic.ventanaColi import *
from logica import *;
#-------------------------------------
#------------- Interfaz---------------

class Ventana_principal(QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        #----------------------------
        self.setWindowTitle("DISPERSION")
        #--------------------------------
        self.ui.tabWidget.setTabText(0,"ENCADENAMIENTO LINEAL")
        self.ui.tabWidget.setTabText(1,"DOBLE HASH")
        self.ui.tabWidget.setTabText(2,"PRUEBA CUADRATICA")
        #--------------------------------------------------
        self.ui.tabWidget_2.setTabText(0,"GRAFICA CURSOR")
        self.ui.tabWidget_2.setTabText(1,"CURSOR")        
        #--------------------------------------------
        self.ui.text_ingresar_3.setAlignment(Qt.AlignHCenter)    
        self.ui.text_ingresar.setClearButtonEnabled(True)
        self.ui.text_ingresar_2.setClearButtonEnabled(True)
        self.ui.text_ingresar_3.setClearButtonEnabled(True)
        self.ui.text_ingresarPrimo.setClearButtonEnabled(True)
        self.ui.text_ingresarPrimo.setAlignment(Qt.AlignHCenter)
        self.ui.boton_eliminar.setEnabled(False)    
        self.ui.text_ingresar_3.setEnabled(False)
        self.ui.text_ingresarPrimo.setEnabled(False)
        self.ui.boton_AgregarPrimo.setEnabled(False)
        #-----------------------------------------------------
        self.ui.boton_eliminar.setStyleSheet("background:#9b9b9b;\n")    
        self.ui.text_ingresar_3.setStyleSheet("background:#9b9b9b;\n")
        self.ui.text_ingresarPrimo.setStyleSheet("background:#9b9b9b;\n")
        self.ui.boton_AgregarPrimo.setStyleSheet("background:#9b9b9b;\n")
        #-------------------------------------------
        self.ui.tablaEncaCabe.setColumnCount(2)
        self.ui.tablaEncaCabe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tablaEncaCurs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tablaDobCurs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)                
        self.ui.tablaCuaCurs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tablaEncaCabe.setVisible(False)
        self.ui.tablaEncaCurs.setVisible(False)
        self.ui.tablaDobCurs.setVisible(False)
        self.ui.tablaCuaCurs.setVisible(False)
        self.ui.tablaEncaLisPos.setVisible(False)
        #-------------------------------------------
        
    def Get_modelo(self):
        return self.modelo

#--------------------------------------
#------------controlador---------------

class Controlador():
    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.boton_dispersar.clicked.connect(lambda: self.ventana.Get_modelo().Dispersar())
        self.ventana.ui.boton_eliminar.clicked.connect(lambda: self.ventana.Get_modelo().Eliminar())
        self.ventana.ui.boton_AgregarPrimo.clicked.connect(lambda:self.ventana.Get_modelo().Cambiarprimo())
#---------------------------------------
#---------------Modelo-----------------
class Modelo ():
    def __init__(self) :
        self.ventana = Ventana_principal(self)
        self.matriz =None
        self.valores_in={}
        self.cursor=None

    def Dispersar(self):
        claves=self.ventana.ui.text_ingresar.text()
        nombres=self.ventana.ui.text_ingresar_2.text()
        if claves!='' and nombres !=''  :
            lista_claves = claves.split(',')
            lista_nombres = nombres.split(',')
            if len(lista_claves)==len(lista_nombres):
                #------------------------------------------
                self.ventana.ui.boton_eliminar.setEnabled(True)    
                self.ventana.ui.text_ingresar_3.setEnabled(True)
                self.ventana.ui.text_ingresarPrimo.setEnabled(True)
                self.ventana.ui.boton_AgregarPrimo.setEnabled(True)
                #-----------------------------------------------------
                self.ventana.ui.boton_eliminar.setStyleSheet("background:#2d89ef;\n")    
                self.ventana.ui.text_ingresar_3.setStyleSheet("background:white;\n")
                self.ventana.ui.text_ingresarPrimo.setStyleSheet("background:white;\n")
                self.ventana.ui.boton_AgregarPrimo.setStyleSheet("background:#2d89ef;\n")        
                #---------------------------------------------------------
                llaves_sin_repetir=[]
                for i in range(len(lista_claves)):
                    if int(lista_claves[i]) not in llaves_sin_repetir:
                        llaves_sin_repetir.append(int(lista_claves[i]))
                        self.valores_in[int(lista_claves[i])]=lista_nombres[i]        
                self.encadenamiento= Encadenamiento_lineal(self.valores_in,llaves_sin_repetir)
                self.encadenamiento.LLenar() 
                self.doble_hash= Doble_hash(self.valores_in,llaves_sin_repetir)
                self.doble_hash.LLenar()
                self.cuadratica=Prueba_cuadratica(self.valores_in,llaves_sin_repetir)
                self.cuadratica.LLenar()
                self.Mostrar_simbolos()
                self.Mostrar_tabla(self.ventana.ui.tablaEncaCurs,self.encadenamiento,['SIGUIENTE','LLAVE'])
                self.Mostrar_tabla(self.ventana.ui.tablaDobCurs,self.doble_hash,['MODULO','LLAVE'])
                self.Mostrar_tabla(self.ventana.ui.tablaCuaCurs,self.cuadratica,['LLAVE','NOMBRE'])
                self.Mostrar_cabezas(self.ventana.ui.tablaEncaLisPos)
            else:
                QMessageBox.warning(self.ventana,"    Advertencia    "," NO COINSIDE LOS TAMAÑOS ")
        else:
            QMessageBox.warning(self.ventana,"    Advertencia    "," DATOS NO VALIDOS ")

    def Cambiarprimo(self):
        valor=self.ventana.ui.text_ingresarPrimo.text()
        if valor!=''and valor.isnumeric():
            if self.encadenamiento.primo<int(valor):
                valor=int(valor)
                self.encadenamiento.primo=valor
                self.doble_hash.primo=valor
                self.cuadratica.primo=valor
                self.encadenamiento.LLenar()
                self.doble_hash.LLenar()
                self.cuadratica.LLenar()
                self.Mostrar_simbolos()
                self.Mostrar_tabla(self.ventana.ui.tablaEncaCurs,self.encadenamiento,['SIGUIENTE','LLAVE'])
                self.Mostrar_tabla(self.ventana.ui.tablaDobCurs,self.doble_hash,['MODULO','LLAVE'])
                self.Mostrar_tabla(self.ventana.ui.tablaCuaCurs,self.cuadratica,['LLAVE','NOMBRE'])
                self.Mostrar_cabezas(self.ventana.ui.tablaEncaLisPos)
            else:
                QMessageBox.warning(self.ventana,"    Advertencia    "," El PRIMO DEBE SER MAYOR AL ACTUAL ")
    
        else:
            QMessageBox.warning(self.ventana,"    Advertencia    "," DATOS NO VALIDOS ")
                


    def Eliminar (self):
        numero =self.ventana.ui.text_ingresar_3.text()
        if numero !='' and numero.isnumeric():
                numero=int(numero)
                if numero in list(self.valores_in.keys()):
                    pos,anteriorpos=self.encadenamiento.Eliminar(None,self.encadenamiento.Get_Cabezalista()[numero%self.encadenamiento.primo],numero)
                    self.encadenamiento.cursor.Eliminar(1,(pos,anteriorpos))
                    pos =self.doble_hash.Eliminar(numero)
                    self.doble_hash.cursor.Eliminar(2,pos)
                    pos =self.cuadratica.Eliminar(numero)
                    self.cuadratica.cursor.Eliminar(3,pos)
                    self.Mostrar_simbolos()
                    self.Mostrar_tabla(self.ventana.ui.tablaEncaCurs,self.encadenamiento,['SIGUIENTE','LLAVE'])
                    self.Mostrar_tabla(self.ventana.ui.tablaDobCurs,self.doble_hash,['MODULO','LLAVE'])
                    self.Mostrar_tabla(self.ventana.ui.tablaCuaCurs,self.cuadratica,['LLAVE','NOMBRE'])
                    self.valores_in.pop(numero)
                    self.ventana.ui.label.setText('Disponible: '+str(self.encadenamiento.cursor.Get_disponible())+','+str(self.doble_hash.cursor.Get_disponible())+','+str(self.cuadratica.cursor.Get_disponible()))
                else:
                    QMessageBox.warning(self.ventana,"     Advertencia    ","      El valor ingresado no se encuentra en la lista       ")
                          
        else:
            QMessageBox.warning(self.ventana,"     Advertencia    ","      El valor ingresado debe ser un numero       ")
        self.ventana.ui.text_ingresar_3.clear()    

    def Mostrar_cabezas(self,tabla):
        lista=[]
        for i in self.encadenamiento.lista:
            if i!=-1 and i!=None:
                lista.append(i.Get_poscion()) 
            else:
                lista.append(-1)
        labels_en_x=[]
        if tabla.rowCount()!=0:
            tabla.clearContents()
            tabla.setRowCount(0)
            tabla.setColumnCount(0)
        for i in range(len(lista)):
            tabla.insertColumn(i)
            tabla.setColumnWidth(i,50)
        if tabla.columnCount()>19:
             tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
             tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabla.insertRow(0)
        tabla.setRowHeight(0,55)    
        
        for j in range(len(lista)) :
            celda= QTableWidgetItem(str(lista[j]))
            celda.setTextAlignment(Qt.AlignHCenter)
            tabla.setItem(0,j,celda)
        tabla.setVerticalHeaderLabels(["POSICION"])
        for i in range(len(self.encadenamiento.lista)):
            labels_en_x.append(str(i))
        tabla.setHorizontalHeaderLabels(labels_en_x)          
        tabla.setVisible(True) 
        
        

    def Mostrar_simbolos(self):
        labels_en_y=[]
        if self.ventana.ui.tablaEncaCabe.rowCount()!=0:
            self.ventana.ui.tablaEncaCabe.clearContents()
            self.ventana.ui.tablaEncaCabe.setRowCount(0)
        self.ventana.ui.tablaEncaCabe.setHorizontalHeaderLabels(["   MODULO ","   LISTA   "])
        fila=0
        for i in self.encadenamiento.imprimir():
            columna=0
            self.ventana.ui.tablaEncaCabe.insertRow(fila)
            for j in i :
                celda= QTableWidgetItem(str(j))
                celda.setTextAlignment(Qt.AlignHCenter)
                self.ventana.ui.tablaEncaCabe.setItem(fila,columna,celda)
                columna+=1
            fila+=1 
        for i in range(len(self.encadenamiento.imprimir())):
            labels_en_y.append(str(i))
        self.ventana.ui.tablaEncaCabe.setVerticalHeaderLabels(labels_en_y)  
        self.ventana.ui.tablaEncaCabe.setVisible(True) 
        
 
    def Mostrar_tabla(self,tabla,metodo,labels_v): 
        labels_en_x=[]
        if tabla.rowCount()!=0:
            tabla.clearContents()
            tabla.setRowCount(0)
            tabla.setColumnCount(0)
        for i in range(len(metodo.cursor.Get_cursor()[0])):
            tabla.insertColumn(i)
            tabla.setColumnWidth(i,50)
        if tabla.columnCount()>19:
             tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
             tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i in range(len(metodo.cursor.Get_cursor())):
            tabla.insertRow(i)
            tabla.setRowHeight(i,55)    
        for i in range(len(metodo.cursor.Get_cursor())):
            for j in range(len(metodo.cursor.Get_cursor()[i])) :
                celda= QTableWidgetItem(str(metodo.cursor.Get_cursor()[i][j]))
                celda.setTextAlignment(Qt.AlignHCenter)
                tabla.setItem(i,j,celda)
        #self.ventana.ui.TablaCursor.setVerticalHeaderLabels(["POSICION","LLAVE","NOMBRE","SIGUIENTE"])
        for i in range(len(metodo.cursor.Get_cursor()[0])):
            labels_en_x.append(str(i))
        tabla.setHorizontalHeaderLabels(labels_en_x)
        tabla.setVerticalHeaderLabels(labels_v)          
        tabla.setVisible(True) 
        
 
    def Get_ventana(self):
        return self.ventana    

#--------------------------------------
#---------------Main------------------- 
if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())
