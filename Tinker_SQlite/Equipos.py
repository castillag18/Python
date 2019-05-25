#Agenda 1

from tkinter import *
from tkinter import messagebox
import Config
import sqlite3

lista = []


def metod():
    

    conexion = sqlite3.connect('ag.sqlite3')
    consulta = conexion.cursor()

    sql = """
    create table tabla2(
    "Nombres"	INTEGER NOT NULL,
	  "Apellidos"	TEXT NOT NULL,
	  "Equipo al cual pertenece"	TEXT NOT NULL,
	  "Pais"	TEXT NOT NULL,
	  "Peso (Kg)"	INTEGER NOT NULL,
	  "Altura (Mts)"	INTEGER NOT NULL,
	  "Id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
    )
    """

    if(consulta.execute(sql)):
        print("Tabla creada")
    else:
        print("Ha ocurrido un error al crear la tabla")

    consulta.close()
    conexion.commit()
    conexion.close()

  
def guardar():     
  n = Nombres.get()     
  ap = Apellidos.get()     
  am = EquipoP.get()     
  c = Peso.get()     
  t = Pais.get()
  al = Altura.get()     
  lista.append(n+"$"+ap+"$"+am+"$"+t+"$"+c)     
  escribirContacto()     
  messagebox.showinfo("Guardado","El jugador ha sido guardado con exito!!!")     
  Nombres.set("")     
  Apellidos.set("")     
  EquipoP.set("")     
  Peso.set("")     
  Pais.set("") 
  Altura.set("")    
  consultar()   

def eliminar():     
    eliminado = conteliminar.get()     
    removido = False     
    for elemento in lista:         
      arreglo = elemento.split("$")         
      if conteliminar.get() == arreglo[6]:             
        lista.remove(elemento)             
        removido = True     
        escribirContacto()     
        consultar()     
        if removido:         
          messagebox.showinfo("Eliminar","Elemento eliminado "+eliminado)          
 
def consultar():     
  r = Text(ventana, width=100, height=15)     
  lista.sort()     
  valores = []     
  r.insert(INSERT, "Nombres\t|\tApellidos \t|\tEquippo al cual pertenece\t|\tPais\t|\tPeso(Kg)\t|\tAltura(Mts)\t|\tId\n")     
  for elemento in lista:              
      arreglo = elemento.split("$")              
      valores.append(arreglo[6])             
      r.insert(INSERT, arreglo[0]+"\t"+arreglo[1]+"\t\t"+ 
                arreglo[2]+"\t\t"+arreglo[3]+"\t\t"+arreglo[4]+"\t\t"+arreglo[5]+"\t\t"+arreglo[6]+"\t\t")     
  r.place(x=20,y=230)     
  spinTelefono = Spinbox(ventana, value=(valores),textvariable=conteliminar).place(x=450, y=50)     
  if lista ==[]: 
    spinTelefono = Spinbox(ventana, value=(valores)).place(x=450,y=50)     
  r.config(state=DISABLED) 

def iniciarArchivo():    
  archivo = open("Ju.txt","a")     
  archivo.close() 
 
def cargar():     
  archivo = open("Ju.txt","r")     
  linea = archivo.readline()     
  if linea:         
    while linea:            
     if linea[-1]=='\n':                 
       linea = linea[:-1]             
       lista.append(linea)             
       linea = archivo.readline()     
       archivo.close() 
 
def escribirContacto():     
  archivo = open("Ju.txt","w")     
  lista.sort()     
  for elemento in lista:         
    archivo.write(elemento+"\n")     
  archivo.close() 

ventana = Tk() 
Nombres = StringVar() 
Apellidos = StringVar() 
EquipoP = StringVar() 
Altura = StringVar() 
Peso = StringVar()
Pais = StringVar() 
conteliminar = StringVar() 
colorFondo = "#e74c3c" 
colorLetra = "#FFF" 
iniciarArchivo() 
cargar() 
consultar() 
ventana.title("Copá America Brazil 2019") 
ventana.geometry("850x500") 
ventana.configure(background = colorFondo) 
etiquetaTitulo = Label(ventana, text="Copá America Brazil 2019", bg=colorFondo, 
  fg=colorLetra).place(x=270,y=10) 
etiquetaN = Label(ventana, text="Nombres", bg=colorFondo,
  fg=colorLetra).place(x=50, y=50) 
cajaN = Entry(ventana, textvariable=Nombres).place(x=150, y=50)
etiquetaApp = Label(ventana, text="Apellidos", bg=colorFondo,
 fg=colorLetra).place(x=50, y=80) 
cajaApp = Entry(ventana, textvariable=Apellidos).place(x=150, y=80) 
etiquetaApm = Label(ventana, text="Equipo", bg=colorFondo,
 fg=colorLetra).place(x=60, y=110) 
cajaApm = Entry(ventana, textvariable=EquipoP).place(x=150, y=110) 
etiquetaT = Label(ventana, text="Pais", bg=colorFondo, 
 fg=colorLetra).place(x=70, y=140) 
cajaT = Entry(ventana, textvariable=Pais).place(x=150, y=140) 
etiquetaC = Label(ventana, text="Peso", bg=colorFondo,
 fg=colorLetra).place(x=70, y=170) 
cajaC = Entry(ventana, textvariable=Peso).place(x=150, y=170) 
etiquetaH = Label(ventana, text="Altura", bg=colorFondo,
 fg=colorLetra).place(x=70, y=170) 
cajaH = Entry(ventana, textvariable=Altura).place(x=150, y=170) 
etiquetaEliminar = Label(ventana, text="Teléfono: ", bg= colorFondo,
  fg=colorLetra).place(x=370, y=50) 
spinTelefono = Spinbox(ventana, textvariable=conteliminar).place(x=450, y=50) 
botoGuardar = Button(ventana, text="Guardar", command=guardar, bg="#009",
 fg="white").place(x=180, y=200) 
botoEliminar = Button(ventana, text="Eliminar", command=eliminar, bg="#009",    
 fg="white").place(x=490, y=80) 

mainloop()


