#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Prueba de UI Qt4

#Se convierte la interfaz de '.ui' a '.py' (el contenido, no solo la extencion
#C:\Python27\Lib\site-packages\PyQt4>pyuic4.bat "MainWindow.ui" -o "design.py"

import sys
from PyQt4 import QtCore, QtGui, uic
#Se importa el modulo con la interfaz
import designUIPY

'''Clase que enlaza el programa con la UI'''
#Se pasa el modulo.elNombreDeLaClaseMain al constructor
class MyWindowClass(QtGui.QMainWindow, designUIPY.Ui_MainWindow):
 def __init__(self, parent=None):
  super(MyWindowClass, self).__init__(parent)
  self.setupUi(self)
  #Establece el diseño y los widgets que se definen (conexta los objetos de la interfaz con el programa)
  self.btn_CtoF.clicked.connect(self.btn_CtoF_clicked)
  self.btn_FtoC.clicked.connect(self.btn_FtoC_clicked)
 
 # Evento del boton btn_CtoF
 def btn_CtoF_clicked(self):
  cel = float(self.editCel.text())
  fahr = cel * 9 / 5.0 + 32
  self.spinFahr.setValue(int(fahr + 0.5))
 
 # Evento del boton btn_FtoC
 def btn_FtoC_clicked(self):
  fahr = self.spinFahr.value()
  cel = ((fahr - 32) * 5) / 9
  self.editCel.setText(str(cel))

''' Inicio del programa'''  
#Funcion Principal
def main():  
  app = QtGui.QApplication(sys.argv)  # nueva instancia de QApplication
  form = MyWindowClass()  # configuramos nuestro formulario para ser usado
  form.show()  # Mostramos el formulario
  app.exec_()  # y ejecutamos la aplicacion
	
if __name__ == '__main__':  # si estamos ejecutando el archivo directamente y no importarlo
   main()  # ejecutar la función principal
