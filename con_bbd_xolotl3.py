# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:42:19 2020

@author: riosv
"""
from tkinter import *
from tkinter import ttk, font
import getpass
import sqlite3 
#creamos la clase opciones para poder heredar a las demas clases
class Parametros:
    def __init__(self):
        self.font="Trebuchet MS"
        self.tamaño_letra=18      
        self.fuentebot= "Helvetica"
        self.ta_letrabut=15
        self.direccion_ico="optixolotl.ico"
        self.titulo1="Acceso\t Opti_Xólotl"
        self.largo=0
        self.ancho=0
        self.men="Bienvenido"
        self.cont="Ingresa\n Usuario y Contraseña por favor\n"
#creamos el atributo conexion a db
        self.conexion=sqlite3.connect("Base_de_datos_Opti_Xólotl.db")
#creamos el cursor el cual nos permitira movernos por la base de datos
        self.cursor=self.conexion.cursor()
        self.conexion.commit()
#creamos el atributo cerrar conexion con db
        self.conexion.close()
        self.fuente ="bold"
        self.tam_font=12
        self.posicion="center"
        self.fuentee="Comic Sans MS"
        self.men2="Bienvenido"
        self.cont2="Acceso concedido\n Excelente dia" 
        self.men3="¡¡Hola!!"
        self.cont3="Registro Exitoso\n"
#metodo para crear la base de datos
    def crear_db(self):
        self.conexion=sqlite3.connect("Base_de_datos_Opti_Xólotl.db")
        self.cursor=self.conexion.cursor()
#metodo para cerrar la base de datos
    def cerrar_db(self):
        self.conexion.commit()
        self.conexion.close()
#metodo para crear la tabla de clientes
    def tabla_cliente(self):
        self.cursor.execute('''Create table if not exists Clientes(
                            Numero_de_cliente integer Primary key autoincrement,
                            Nombre text,
                            Apellido_Paterno text,
                            Apellido_Materno text,
                            Direccion text,
                            Telefono text,
                            Enfermedades text,
                            Graduacion text,
                            Armazon_o_lentes text,
                            Edad integer,
                            Costo Integer,
                            Paga Integer,
                            Debe Integer,
                            Clave_micas text,
                            Clave_estuches text)''')
    def tabla_armazon(self):
        self.cursor.execute('''
                            Create table if not exists Armazones(
                            Clave text Primary Key,
                            Armazon text,
                            Piezas integer)
                            ''')
    def tabla_micas(self):
        self.cursor.execute('''Create table if not exists Micas(Clave text Primary Key,
                            Mica text,
                            Piezas integer)''')
    def tabla_lentes_contacto(self):
        self.cursor.execute('''Create table if not exists Lentes_contacto(Clave text Primary Key,
                            Lentes text,
                            Piezas integer)''')
    def tabla_estuches(self):
        self.cursor.execute('''Create table if not exists Estuches(Clave text Primary key,
                            Estuche text,
                            Piezas Integer)''')
#Clase aplicacion con todos los metodos y atributos de la clase opciones, heredados 
class Aplicacion(Parametros):
    def __init__(self):
#Primer ventana, ventana de acceso, con sus propios atributos y su unico metodo
        Parametros.__init__(self)
        self.raiz = Tk()
        self.raiz.geometry("410x210")
        self.raiz.resizable(self.largo,self.ancho)
        self.raiz.title("Acceso\t\t Opti_Xólotl")
        self.raiz.iconbitmap(self.direccion_ico)
        self.mensaje=messagebox.showinfo(self.men,self.cont)
        self.raiz.config(bg="pink")                       
        self.etiq1 = Label(self.raiz, text="Usuario:",bg="Pink",font=(self.fuente,self.tamaño_letra))
        self.etiq2 = Label(self.raiz, text="Contraseña:",bg="Pink", font=(self.fuente,self.tamaño_letra))
        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.raiz, textvariable=self.mensa, font=self.fuente, foreground='blue')
        self.usuario = StringVar()
        self.clave = StringVar()
        self.usuario.set("")
        self.ctext1 = ttk.Entry(self.raiz,textvariable=self.usuario, width=26,font=(self.fuente,self.tam_font))
        self.ctext2 = ttk.Entry(self.raiz, textvariable=self.clave, width=26,show="*",font=(self.fuente,self.tam_font))
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        self.boton1 = Button(self.raiz, text="Aceptar",padx=5,pady=5, command=self.aceptar,font=(self.fuentebot,self.ta_letrabut),fg="red")
        self.boton3 = Button(self.raiz, text="Salir",padx=5,pady=5, command=self.raiz.destroy,font=(self.fuentebot,self.ta_letrabut),fg="red")
        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=125, y=42)
        self.ctext2.place(x=166, y=82)
        self.separ1.place(x=5, y=145, bordermode=OUTSIDE,height=10, width=420)
        self.boton1.place(x=50, y=160)
        self.boton3.place(x=200, y=160)
        self.ctext1.focus_set()
    #mantiene la ventana Tk abierta hasta que obtenga la instruccion de destruirse
        self.raiz.mainloop()
#con el getpass, verificamos con ayuda del boton aceptar para verificar que se cumpla que esta correcto el usuario y contraseña
    def aceptar(self):
        if self.usuario.get() == 'knch1':
            if self.clave.get()=='CCHavez2':
                self.etiq3.configure(foreground='blue')
                self.mensa.set("Acceso permitido")
#destruimos la ventana de acceso
                self.raiz.destroy()
#abrimos el objeto menu
                op=Menu()
            else:
                self.etiq3.configure(foreground='red')
                self.mensa.set("Acceso denegado") 
                self.r=messagebox.showinfo("Advertencia","El Usuario o Contraseña es incorrecto\n Intenta lo nuevamente")
                self.ctext2.delete(0,END)
                self.ctext1.delete(0,END)
                self.ctext1.focus_set()
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Acceso denegado")
            self.r=messagebox.showinfo("Advertencia","El Usuario o Contraseña es incorrecto\n Intenta lo nuevamente")
            self.ctext2.delete(0,END)
            self.ctext1.delete(0,END)
            self.ctext1.focus_set()
#_______________________________________________________________________OBJETO**MENU**______________________________________________________
class Menu(Parametros):
    def __init__(self):
        Parametros.__init__(self)
        self.raiz2 = Tk()
        self.raiz2.title("Menu Opti Xólotl")
        self.raiz2.iconbitmap(self.direccion_ico)
        self.raiz2.resizable(self.largo,self.ancho)
        self.frame2 = Frame(self.raiz2,width="680",height="400")
        self.frame2.pack()
        self.frame2.config(bg="Pink")
        mensaje=messagebox.showwarning("Adevertencia","Ingresa primero a tu almacen\nEn caso de que nunca hallas registrado un articulo")
        self.labelbienvenida = Label(self.frame2,text="¡¡Bievenido!!\n Aqui encontraras las opciones a las cuales puedes acceder",bg="Pink",fg="Purple",font=("Comic Sans MS",18)).place(x=5,y=10)
        self.labelcliente = Label(self.frame2,text="Ingresar Cliente",bg="Pink",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=20,y=100)
        self.botonacceder1=Button(self.frame2,text="Acceder",font=(self.fuentebot,self.tam_font),fg="red",justify=self.posicion,command=self.entclientes).place(x=70,y=150)
        self.labelconsultarcliente = Label(self.frame2,text="Consultar Clientes",bg="Pink",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=350,y=100)
        self.botonacceder2=Button(self.frame2,text="Acceder",font=(self.fuentebot,self.tam_font),fg="red",justify=self.posicion,command=self.entcclientes).place(x=400,y=150)
        self.labelingresaralmacen = Label(self.frame2,text="Ingresar al Almacen",bg="Pink",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=350,y=200)
        self.botonacceder3 = Button(self.frame2,text="Acceder",font=(self.fuentebot,self.tam_font),fg="red",justify=self.posicion,command=self.entalmacen).place(x=400,y=250)
        self.labelconsultaralmacen = Label(self.frame2,text="Consultar Almacen",bg="Pink",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=20,y=200)
        self.botonacceder4 = Button(self.frame2,text="Acceder",font=(self.fuentebot,self.tam_font),fg="red",justify=self.posicion,command=self.entcalmacen).place(x=70,y=250)
        self.labelsalirprograma=Label(self.frame2,text="Salir del programa",bg="Pink",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=200,y=300)
        botonsalir=Button(self.frame2,text="Salir",font=(self.fuentebot,self.tam_font),fg="red",justify=self.posicion,command=self.raiz2.destroy).place(x=250,y=350)
        self.raiz2.mainloop()
    def entclientes(self):
        self.raiz2.destroy()
        l=Cliente()
    def entcclientes(self):
        self.raiz2.destroy()
        n=Ccliente()
    def entalmacen(self):
        self.raiz2.destroy()
        r=Almacen()
    def entcalmacen(self):
        self.raiz2.destroy()
        f=Calmacen()
#_______________________________________________________________________OBJETO****CLIENTE_______________________________________________________
class Cliente(Parametros):
    def __init__(self):
        Parametros.__init__(self)
        self.raiz3 = Tk()
        self.raiz3.title("Registro de Clientes Xólotl")
        self.raiz3.iconbitmap(self.direccion_ico)
        self.raiz3.resizable(self.ancho,self.largo)
        self.frame3 = Frame(self.raiz3,width="1000",height="800")
        self.frame3.pack()
        self.frame3.config(bg="pink")
        self.nom = StringVar()
        self.apellidop = StringVar()
        self.apellidom = StringVar()
        self.dire = StringVar()
        self.tel = IntVar()
        self.enf = StringVar()
        self.grad = StringVar()
        self.pedido = StringVar()
        self.edad = IntVar()
        self.costo= IntVar()
        self.paga=IntVar()
        self.material= StringVar()
        self.correo = StringVar()
        self.nom.set("")
        self.apellidop.set("")
        self.apellidom.set("")
        self.dire.set("")
        self.enf.set("")
        self.grad.set("")
        self.pedido.set("")
        self.material.set("")
        self.correo.set("")
        self.saludo=Label(self.frame3,text="¡Hola nuevamente!\nIngresa la información de tus clientes",bg="Pink",fg="Purple",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=10)
        self.labelnombre=Label(self.frame3,text="Nombre:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=100)
        self.Cuadronombre = ttk.Entry(self.frame3, textvariable= self.nom,font=self.fuente,width=26)
        self.labelapellidop=Label(self.frame3,text="Apellido paterno:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=150)
        self.Cuadroapellidop = ttk.Entry(self.frame3, textvariable= self.apellidop,font=self.fuente,width=26)
        self.labelapellidom=Label(self.frame3,text="Apellido materno:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=200)
        self.Cuadroapellidom = ttk.Entry(self.frame3, textvariable=self.apellidom,font=self.fuente,width=26)
        self.labeldireccion=Label(self.frame3,text="Dirección:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=250)
        self.Cuadrodireccion =  ttk.Entry(self.frame3, textvariable=self.dire,font=self.fuente,width=30)
        self.labeltelefono=Label(self.frame3,text="Telefono:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=300)
        self.Cuadrotelefono = ttk.Entry(self.frame3,textvariable=self.tel,font=self.fuente,width=26)
        self.labelenfermedades=Label(self.frame3,text="Enfermedades:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=350)
        self.Cuadroenfermedades=ttk.Entry(self.frame3,textvariable=self.enf,font=self.fuente,width=26)
        self.labelgraduacion=Label(self.frame3,text="Graduación:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=400)
        self.Cuadrograduacion=ttk.Entry(self.frame3,textvariable=self.grad,font=self.fuente,width=26)
        self.labelpedido=Label(self.frame3,text="Clave armazon o lentes:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=450)
        self.Cuadropedido=ttk.Entry(self.frame3,textvariable=self.pedido,font=self.fuente,width=26)
        self.labeledad=Label(self.frame3,text="Edad:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=500)
        self.Cuadroedad=ttk.Entry(self.frame3,textvariable=self.edad,font=self.fuente,width=26)
        self.labelcosto=Label(self.frame3,text="Costo:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=550)
        self.Cuadrocosto=ttk.Entry(self.frame3,textvariable=self.costo,font=self.fuente,width=26)
        self.labelpaga=Label(self.frame3,text="Paga:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=600)
        self.Cuadropaga=ttk.Entry(self.frame3,textvariable=self.paga,font=self.fuente,width=26)
        self.labelmaterial=Label(self.frame3,text="Clave mica:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=650)
        self.Cuadromaterial=ttk.Entry(self.frame3,textvariable=self.material,font=self.fuente,width=30)
        self.labelcorreo=Label(self.frame3,text="Clave estuche:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=10,y=700)
        self.Cuadrocorreo=ttk.Entry(self.frame3,textvariable=self.correo,font=self.fuente,width=26)
        self.registrar=Button(self.frame3,text="Registrar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="red",command=self.guardarclientes).place(x=50,y=750)
        self.regresar2=Button(self.frame3,text="Regresar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="red",command=self.volver).place(x=200,y=750)
        self.salir2=Button(self.frame3,text="Salir",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="red",command=self.raiz3.destroy).place(x=350,y=750)
        self.Cuadronombre.place(x=112,y=100)
        self.Cuadroapellidop.place(x=209,y=150)
        self.Cuadroapellidom.place(x=213,y=200)
        self.Cuadrodireccion.place(x=129,y=250)
        self.Cuadrotelefono.place(x=125,y=300)
        self.Cuadroenfermedades.place(x=189,y=350)
        self.Cuadrograduacion.place(x=147,y=400)
        self.Cuadropedido.place(x=280,y=450)
        self.Cuadroedad.place(x=82,y=500)
        self.Cuadrocosto.place(x=87,y=550)
        self.Cuadropaga.place(x=84,y=600)
        self.Cuadromaterial.place(x=140,y=650)
        self.Cuadrocorreo.place(x=180,y=700)
        self.Cuadronombre.focus_set()
        self.raiz3.mainloop()
    def volver(self):
        self.raiz3.destroy()
        op=Menu()
    def borrarcl(self):
        self.Cuadronombre.delete(0, END )
        self.Cuadroapellidop.delete(0, END )
        self.Cuadroapellidom.delete(0, END )
        self.Cuadrodireccion.delete(0, END )
        self.Cuadrotelefono.delete(0, END )
        self.Cuadroenfermedades.delete(0, END )
        self.Cuadrograduacion.delete(0, END )
        self.Cuadropedido.delete(0, END )
        self.Cuadroedad.delete(0, END )
        self.Cuadrocosto.delete(0, END )
        self.Cuadropaga.delete(0, END )
        self.Cuadromaterial.delete(0, END )
        self.Cuadrocorreo.delete(0, END )
        self.Cuadronombre.focus_set()
    def guardarclientes(self):
        if(self.nom.get()=="" or self.apellidop.get()=="" or self.apellidom.get()=="" or self.dire.get()=="" or self.enf.get()=="" or self.tel.get()==0 or self.grad.get()=="" or self.pedido.get()=="" or self.edad.get()==0  or self.costo.get()==0 or self.paga.get()==0 or self.material.get()=="" or self.correo.get()==""):
            if(self.nom.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadronombre.focus_set()
            if(self.apellidop.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadroapellidop.focus_set()
            if(self.apellidom.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadroapellidom.focus_set()
            if(self.dire.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadrodireccion.focus_set()
            if(self.enf.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadrotelefono.focus_set()
            if(self.tel.get()==0):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadroenfermedades.focus_set()
            if(self.grad.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadrograduacion.focus_set()
            if(self.pedido.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadropedido.focus_set()
            if(self.edad.get()==0):
                if(self.edad.get()==""):
                    self.n=messagebox.showinfo("Error","Ingresa numeros enteros")
                    self.Cuadroedad.focus_set()
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadroedad.focus_set()
            if(self.costo.get()==0):
                if(self.costo.get()==""):
                    self.n=messagebox.showinfo("Error","Ingresa numeros enteros")
                self.Cuadroedad.focus_set()
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadrocosto.focus_set()
            if(self.paga.get()==0):
                if(self.paga.get()==""):
                    self.n=messagebox.showinfo("Error","Ingresa numeros enteros")
                    self.Cuadroedad.focus_set()
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadropaga.focus_set()
            if(self.material.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadromaterial.focus_set()
            if(self.correo.get()==""):
                self.n=messagebox.showinfo("Error","Todos los campos son obligatorios")
                self.Cuadrocorreo.focus_set()
        else:
                
            if(self.costo.get()<=self.paga.get()):
                cambio=(self.paga.get()-self.costo.get())
                mensajecambio=messagebox.showinfo("El cambio es de:",cambio)
                self.m3=messagebox.showinfo(self.men3,self.cont3)
                self.crear_db()
                self.tabla_cliente()
                self.nada=0
                self.clientes=[(self.nom.get(),self.apellidop.get(),self.apellidom.get(),self.dire.get(),self.enf.get(),self.tel.get(),self.grad.get(),self.pedido.get(),self.edad.get(),self.costo.get(),self.paga.get(),self.nada,self.material.get(),self.correo.get())]
                self.cursor.executemany("INSERT INTO Clientes VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self.clientes)
                self.conexion.commit()
                if(self.pedido.get()=="esf01" or self.pedido.get()=="tiri02"):
                    consulta1=[(self.pedido.get())]
                    self.cursor.execute("SELECT * FROM  Lentes_contacto WHERE Clave=?",consulta1)
                    for lentes in self.cursor:
                        piezaslentes=1
                        lente=lentes[2]
                        piezaslentes_nuevos=(lente-piezaslentes)
                        self.cursor.execute('''UPDATE Lentes_contacto SET  Piezas=? WHERE Clave=? ''',(piezaslentes_nuevos,self.pedido.get()))
                        self.conexion.commit()  
                    self.conexion.close()  
                    self.borrarcl()
                if(self.pedido.get()=="meta01" or self.pedido.get()=="past02" or self.pedido.get()=="ran03" or self.pedido.get()=="3pi04"):
                    consulta1=[(self.pedido.get())]
                    consulta2=[(self.material.get())]
                    consulta3=[(self.correo.get())]
                    self.cursor.execute("SELECT * FROM  Armazones WHERE Clave=?",consulta1)
                    for piezas in self.cursor:
                        piezasr=1
                        pieza=piezas[2]
                        nueva_pieza=(pieza-piezasr)
                        self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=? ''',(nueva_pieza,self.pedido.get()))
                        self.conexion.commit()                        
                    self.cursor.execute("SELECT * FROM Micas WHERE Clave=?",consulta2)
                    for piezasmicas in self.cursor:
                        piezaares=1
                        piezaca=piezasmicas[2]
                        pieza_nueva=(piezaca-piezaares)
                        self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=? ''',(pieza_nueva,self.material.get()))
                        self.conexion.commit() 
                    self.cursor.execute("SELECT * FROM Estuches WHERE Clave=?",consulta3)
                    for estuches in self.cursor:
                        piezamenos=1
                        piezascom=estuches[2]
                        actualizacion=(piezascom-piezamenos)
                        self.cursor.execute('''UPDATE Estuches SET  Piezas=? WHERE Clave=? ''',(actualizacion,self.correo.get()))
                        self.conexion.commit()         
                    self.conexion.close()
                    self.borrarcl() 
            else:
                self.debe=(self.costo.get()-self.paga.get())
                self.deb=messagebox.showinfo("Debe",self.debe)
                self.crear_db()
                self.tabla_cliente()
                self.clientes=[(self.nom.get(),self.apellidop.get(),self.apellidom.get(),self.dire.get(),self.enf.get(),self.tel.get(),self.grad.get(),self.pedido.get(),self.edad.get(),self.costo.get(),self.paga.get(),self.debe,self.material.get(),self.correo.get())]
                self.cursor.executemany("INSERT INTO Clientes VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",self.clientes)
                self.conexion.commit()
                if(self.pedido.get()=="esf01" or self.pedido.get()=="tiri02"):
                    consulta1=[(self.pedido.get())]
                    self.cursor.execute("SELECT * FROM  Lentes_contacto WHERE Clave=?",consulta1)
                    for lentes in self.cursor:
                        piezaslentes=1
                        lente=lentes[2]
                        piezaslentes_nuevos=(lente-piezaslentes)
                        self.cursor.execute('''UPDATE Lentes_contacto SET  Piezas=? WHERE Clave=? ''',(piezaslentes_nuevos,self.pedido.get()))
                        self.conexion.commit()  
                    self.conexion.close() 
                    self.borrarcl()
                if(self.pedido.get()=="meta01" or self.pedido.get()=="past02" or self.pedido.get()=="ran03" or self.pedido.get()=="3pi04"):
                    consulta1=[(self.pedido.get())]
                    consulta2=[(self.material.get())]
                    consulta3=[(self.correo.get())]
                    self.cursor.execute("SELECT * FROM  Armazones WHERE Clave=?",consulta1)
                    for piezas in self.cursor:
                        piezasr=1
                        pieza=piezas[2]
                        nueva_pieza=(pieza-piezasr)
                        self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=? ''',(nueva_pieza,self.pedido.get()))
                        self.conexion.commit()                        
                    self.cursor.execute("SELECT * FROM Micas WHERE Clave=?",consulta2)
                    for piezasmicas in self.cursor:
                        piezaares=1
                        piezaca=piezasmicas[2]
                        pieza_nueva=(piezaca-piezaares)
                        self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=? ''',(pieza_nueva,self.material.get()))
                        self.conexion.commit() 
                    self.cursor.execute("SELECT * FROM Estuches WHERE Clave=?",consulta3)
                    for estuches in self.cursor:
                        piezamenos=1
                        piezascom=estuches[2]
                        actualizacion=(piezascom-piezamenos)
                        self.cursor.execute('''UPDATE Estuches SET  Piezas=? WHERE Clave=? ''',(actualizacion,self.correo.get()))
                        self.conexion.commit()         
                    self.conexion.close()
                    self.borrarcl()            
                self.m3=messagebox.showinfo(self.men3,self.cont3)
#________________________________________________________________________OBJETO**CONSULTA**CLIENTE________________________________________________________________________________________________
class Ccliente(Parametros):
    def __init__(self):
        Parametros.__init__(self)
        self.raiz4=Tk()
        self.raiz4.title("Consulta de Clientes Xólotl")
        self.raiz4.iconbitmap(self.direccion_ico)
        self.raiz4.resizable(1,1)
        self.frame4=Frame(self.raiz4,width="1800",height="800")
        self.frame4.pack()
        self.frame4.config(bg="MistyRose3")
        self.numero=IntVar()
        self.mensaje=Label(self.frame4,text="Aqui podras consultar el seguimiento de tus clientes",fg="blue",font=("Comic Sans MS",18)).place(x=10,y=5)
        self.numerocliente=Label(self.frame4,text="Numero de cliente:",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=55)
        self.Cuadrotcliente=ttk.Entry(self.frame4,textvariable=self.numero,font=self.fuente)
        self.labelnombre=Label(self.frame4,text="Nombre de cliente:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=100)
        self.labelapellidopat=Label(self.frame4,text="Apellido paterno:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=145)
        self.labelapellidomat=Label(self.frame4,text="Apellido materno:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=190)
        self.labeldireccioon=Label(self.frame4,text="Direccion:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=235)
        self.labeltel=Label(self.frame4,text="Telefono:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=280)
        self.labelenf=Label(self.frame4,text="Enfermedades:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=325)
        self.labelgrad=Label(self.frame4,text="Graduación:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=370)
        self.labelped=Label(self.frame4,text="Clave armazon:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=415)
        self.labeledad=Label(self.frame4,text="Edad:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=460)
        self.labelcosto=Label(self.frame4,text="Costo:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=505)
        self.labelpagaa=Label(self.frame4,text="Paga:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=550)
        self.labeldebe=Label(self.frame4,text="Debe:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=595)
        self.labelmat=Label(self.frame4,text="Clave mica:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=640)
        self.labelped=Label(self.frame4,text="Clave estuche:",bg="MistyRose3",fg="black",font=(self.fuentee,self.tamaño_letra)).place(x=15,y=685)
        self.boconsultar=Button(self.frame4,text="Consultar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.consultarclientes).place(x=350,y=730)
        self.borrarcliente=Button(self.frame4,text="Borrar cliente",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.borrarclien).place(x=520,y=730)
        self.regresar=Button(self.frame4,text="Regresar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.volver1).place(x=5,y=730)
        self.salir=Button(self.frame4,text="Salir",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.raiz4.destroy).place(x=1200,y=730)
        self.actualizacionar=Button(self.frame4,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.actualizar).place(x=890,y=730)
        self.Cuadrotcliente.place(x=231,y=60)
        self.Cuadrotcliente.focus_set()
        self.raiz4.mainloop()
 #metodo para destruir la ventana actual y crear nuevamente la ventana menu
    def volver1(self):
        self.raiz4.destroy()
        op=Menu()
#metodo para relizar consultas en la base de datos
    def consultarclientes(self):
        if(self.numero.get()==0):
            mensajedeerror=messagebox.showwarning("Advertencia","Ingresa el numero de cliente")
            self.Cuadrotcliente.focus_set()
        else:
            self.crear_db() 
            self.num=[(self.numero.get())]
            self.cursor.execute("SELECT * FROM Clientes WHERE Numero_de_cliente=?",self.num)
            for cliente in self.cursor:
                consulta1=cliente[1]
                consulta2=cliente[2]
                consulta3=cliente[3]
                consulta4=cliente[4]
                consulta5=cliente[5]
                consulta6=cliente[6]
                consulta7=cliente[7]
                consulta8=cliente[8]
                consulta9=cliente[9]
                consulta10=cliente[10]
                consulta11=cliente[11]
                consulta12=cliente[12]
                consulta13=cliente[13]            
                consulta14=cliente[14]
                vislabel=Label(self.frame4,text=consulta1,bg="MistyRose3",fg="blue",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=100)
                vislabel2=Label(self.frame4,text=consulta2,bg="MistyRose3",fg="blue",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=145)
                vislabel3=Label(self.frame4,text=consulta3,bg="MistyRose3",fg="blue",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=190)
                vislabel4=Label(self.frame4,text=consulta4,bg="MistyRose3",fg="blue",width=60,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=235)
                vislabel5=Label(self.frame4,text=consulta6,bg="MistyRose3",fg="blue",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=280)
                vislabel6=Label(self.frame4,text=consulta5,bg="MistyRose3",fg="blue",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=325)
                vislabel7=Label(self.frame4,text=consulta7,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=250,y=370)
                vislabel8=Label(self.frame4,text=consulta8,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=415)
                vislabel9=Label(self.frame4,text=consulta9,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=460)
                vislabel10=Label(self.frame4,text=consulta10,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=505)
                vislabel11=Label(self.frame4,text=consulta11,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=550)
                vislabel12=Label(self.frame4,text=consulta12,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=595)
                vislabel13=Label(self.frame4,text=consulta13,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=640)
                vislabel14=Label(self.frame4,text=consulta14,bg="MistyRose3",fg="blue",width=10,font=(self.fuentee,self.tamaño_letra)).place(x=200,y=685)
            self.Cuadrotcliente.delete(0,END)
            self.Cuadrotcliente.focus_set()
            self.conexion.close()
    def actualizar(self):
        if(self.numero.get()==0):
            mensajedeerror2=messagebox.showwarning("Advertencia","Ingresa el numero de cliente")
            self.Cuadrotcliente.focus_set()
        else:
            self.crear_db() 
            self.num=[(self.numero.get())]
            self.cursor.execute("SELECT * FROM Clientes WHERE Numero_de_cliente=?",self.num)
            for cliente in self.cursor:
                self.consulta13=cliente[12]
                self.grad=StringVar()
                self.pagaa=IntVar()
                self.grad.set("")
                vislabel=Label(self.frame4,text="Graduacion",bg="MistyRose3",fg="pink",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=1000,y=50)
                self.cuadrovista=ttk.Entry(self.frame4,textvariable=self.grad,font=self.fuente) 
                vislabel2=Label(self.frame4,text="Paga",bg="MistyRose3",fg="pink",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=1000,y=150)
                self.cuadrovista2=ttk.Entry(self.frame4,textvariable=self.pagaa,font=self.fuente)
                self.cuadrovista.place(x=1250,y=50)
                self.cuadrovista2.place(x=1250,y=150)
                actualizarpago=Button(self.frame4,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.actualiza_grad).place(x=1200,y=100)
                actualizargraduacion=Button(self.frame4,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),justify=self.posicion,fg="blue",command=self.actualiza_pago).place(x=1200,y=200)
    def actualiza_pago(self):
        if(self.numero.get()==0):
            error2=messagebox.showwarning("Error","Ingresa el numero de cliente")
            self.Cuadrotcliente.focus_set()
        else:
            if(self.pagaa.get()==0):
                otromensaje=messagebox.showwarning("Advertencia","Ingresa la cantidad que paga")
                self.Cuadrovista2.focus_set()
            else:
                if(self.pagaa.get()>=self.consulta13):
                    self.pago=(self.pagaa.get()-self.consulta13)
                    if(self.pago>0):
                        self.pagofinal=0
                        mensajee=messagebox.showinfo("Su cambio es de:",self.pagaa.get()-self.consulta13)
                        self.crear_db()
                        self.cursor.execute('''UPDATE Clientes SET Debe=? WHERE Numero_de_cliente=?''',(self.pagofinal,self.numero.get()))
                        self.conexion.commit()
                        mensajedeexito=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                        self.conexion.close()
                        self.cuadrovista2.delete(0,END)
                        self.Cuadrotcliente.delete(0,END)
                        self.Cuadrotcliente.focus_set()
                    elif(self.pago==0):
                        self.crear_db()
                        self.cursor.execute('''UPDATE Clientes SET Debe=? WHERE Numero_de_cliente=?''',(self.pago,self.numero.get()))
                        self.conexion.commit()
                        mensajedeexito=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                        self.conexion.close()
                        self.cuadrovista2.delete(0,END)
                        self.Cuadrotcliente.delete(0,END)
                        self.Cuadrotcliente.focus_set()
                if(self.pagaa.get()<self.consulta13):
                    self.pago2=(self.consulta13-self.pagaa.get())
                    self.crear_db()
                    self.cursor.execute('''UPDATE Clientes SET Debe=? WHERE Numero_de_cliente=?''',(self.pago2,self.numero.get()))
                    self.conexion.commit()
                    mensajedeexito=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.conexion.close()
                    self.cuadrovista2.delete(0,END)
                    self.Cuadrotcliente.delete(0,END)
                    self.Cuadrotcliente.focus_set()                
    def actualiza_grad(self):
        if(self.numero.get()==0):
            error=messagebox.showwarning("Error","Ingresa el numero de cliente")
            self.Cuadrotcliente.focus_set()
        else:
            if(self.grad.get()==""):
                mensajeee=messagebox.showwarning("Error","Ingresa la graduacion")
            else:
                self.crear_db()
                self.cursor.execute('''UPDATE Clientes SET Graduacion=? WHERE Numero_de_cliente=?''',(self.grad.get(),self.numero.get()))
                self.conexion.commit()
                mensajedeexito=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                self.conexion.close()
                self.cuadrovista.delete(0,END)
                self.Cuadrotcliente.delete(0,END)
                self.Cuadrotcliente.focus_set()
    def borrarclien(self):
        if(self.numero.get()==0):
            mensaje=messagebox.showwarning("Error","Ingresa el numero de cliente")
            self.Cuadrotcliente.focus_set()
        else:
            self.crear_db()
            self.num=[(self.numero.get())]
            self.cursor.execute('''DELETE  FROM Clientes WHERE Numero_de_cliente=?''',self.num)
            self.cerrar_db()
            mensaje1=messagebox.showinfo("Felicitaciones","El cliente se elimino con exito")
            self.Cuadrotcliente.delete(0,END)
            self.Cuadrotcliente.focus_set()
#______________________________________________________________________OBJETO***ALMACEN____________________________________________________________________
class Almacen(Parametros):
    def __init__(self):
        Parametros.__init__(self)
        self.raiz6=Tk()
        self.raiz6.title("Almacen Xólotl")
        self.raiz6.iconbitmap(self.direccion_ico)
        self.raiz6.resizable(self.ancho,self.largo)
        self.frame6=Frame(self.raiz6,width="1000",height="500")
        self.frame6.pack()
        self.frame6.config(bg="RoyalBlue1")
        self.armazon=StringVar()
        self.micas=StringVar()
        self.estuche=StringVar()
        self.lentes_contact=StringVar()
        self.clave=StringVar()
        self.armazon.set("")
        self.micas.set("")
        self.estuche.set("")
        self.lentes_contact.set("")
        self.piezas=IntVar()
        self.piezas2=IntVar()
        self.piezas3=IntVar()
        self.piezas4=IntVar()
        self.clave.set("")
        self.labelarmazon=Label(self.frame6,text="Armazon:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=5)
        self.Cuadroarmazon=ttk.Entry(self.frame6,textvariable=self.armazon,width=30,font=self.fuente)
        self.labelpiezas=Label(self.frame6,text="Piezas",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=55)
        self.Cuadropiezas=ttk.Entry(self.frame6,textvariable=self.piezas,width=30,font=self.fuente)
        self.labelmicas=Label(self.frame6,text="Micas:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=100)
        self.Cuadromicas=ttk.Entry(self.frame6,textvariable=self.micas,width=30,font=self.fuente)
        self.Labelpiezas2=Label(self.frame6,text="Piezas",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=150)
        self.Cuadropiezas2=ttk.Entry(self.frame6,textvariable=self.piezas2,width=30,font=self.fuente)
        self.labellentes=Label(self.frame6,text="lentes de contacto:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=200)
        self.Cuadrolentes=ttk.Entry(self.frame6,textvariable=self.lentes_contact,width=30,font=self.fuente)
        self.labelpiezas3=Label(self.frame6,text="Piezas",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=250)
        self.Cuadropiezas3=ttk.Entry(self.frame6,textvariable=self.piezas3,width=30,font=self.fuente)
        self.labelestuche=Label(self.frame6,text="Estuche:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=300)
        self.Cuadroestuches=ttk.Entry(self.frame6,textvariable=self.estuche,width=30,font=self.fuente)
        self.labelpiezas4=Label(self.frame6,text="Piezas:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=350)
        self.Cuadropiezas4=ttk.Entry(self.frame6,textvariable=self.piezas4,width=30,font=self.fuente)          
        self.labelclave=Label(self.frame6,text="Clave:",fg="purple2",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=400)
        self.Cuadroclave=ttk.Entry(self.frame6,textvariable=self.clave,width=30,font=self.fuente)
        self.registrararmazon=Button(self.frame6,text="Registrar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.armazones).place(x=500,y=25)
        self.registrarmicas=Button(self.frame6,text="Registrar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.mica).place(x=500,y=125)
        self.registrarlentes=Button(self.frame6,text="Registrar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.lentes).place(x=500,y=250)
        self.registrarestuches=Button(self.frame6,text="Registrar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.estuches).place(x=500,y=325)
        self.actualizararmazones=Button(self.frame6,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.actualizarmazon).place(x=640,y=25)
        self.actualizarmicas=Button(self.frame6,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.actualizarmica).place(x=640,y=125)
        self.actualizarlentes=Button(self.frame6,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.actualizarlentes).place(x=640,y=250)
        self.actualizaestuches=Button(self.frame6,text="Actualizar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.actualizarestuches).place(x=640,y=325)
        self.botsalir=Button(self.frame6,text="Salir",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.raiz6.destroy).place(x=270,y=450)
        self.regresar1=Button(self.frame6,text="Regresar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.volver3).place(x=150,y=450)
        self.Cuadroarmazon.place(x=118,y=5)
        self.Cuadropiezas.place(x=84,y=55)
        self.Cuadromicas.place(x=84,y=100)
        self.Cuadropiezas2.place(x=84,y=150)
        self.Cuadrolentes.place(x=225,y=200)
        self.Cuadropiezas3.place(x=85,y=250)
        self.Cuadroestuches.place(x=110,y=300)
        self.Cuadropiezas4.place(x=90,y=350)
        self.Cuadroclave.place(x=85,y=400)
        self.Cuadroarmazon.focus_set()
        self.raiz6.mainloop() 
    def volver3(self):
        self.raiz6.destroy()
        op=Menu()
    def armazones(self):
        if(self.armazon.get()==""):
            errormensaje3=messagebox.showwarning("Error","Ingresa el tipo de armazon")
            self.Cuadroarmazon.focus_set()
        else:
            if(self.armazon.get()=="metalico" or self.armazon.get()=="Metalico"):
                self.clave1="meta01"
                if(self.piezas.get()==0 or self.armazon.get()==""):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()
                else:
                    self.crear_db()
                    self.tabla_armazon()
                    self.dato=[(self.clave1,self.armazon.get(),self.piezas.get())]
                    self.cursor.executemany("INSERT INTO Armazones VALUES(?,?,?)",self.dato)
                    self.cerrar_db()
                    self.n=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t meta01")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()              
            if(self.armazon.get()=="pasta" or self.armazon.get()=="Pasta"):
                self.clave2="past02"
                if(self.piezas.get()==0 or self.armazon.get()==""):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()
                else:
                    self.crear_db()
                    self.tabla_armazon()
                    self.dato=[(self.clave2,self.armazon.get(),self.piezas.get())]
                    self.cursor.executemany("INSERT INTO Armazones VALUES(?,?,?)",self.dato)
                    self.cerrar_db()
                    self.n=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t past02")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()                
            if(self.armazon.get()=="ranurado" or self.armazon.get()=="Ranurado"):
                self.clave3="ran03"
                if(self.piezas.get()==0 or self.armazon.get()==""):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()
                else:
                    self.crear_db()
                    self.tabla_armazon()
                    self.dato=[(self.clave3,self.armazon.get(),self.piezas.get())]
                    self.cursor.executemany("INSERT INTO Armazones VALUES(?,?,?)",self.dato)
                    self.cerrar_db()
                    self.n=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t ran03")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()                
            if(self.armazon.get()=="3piezas" or self.armazon.get()=="3Piezas" ):
                self.clave4="3pi04"
                if(self.piezas.get()==0 or self.armazon.get()==""):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()
                else:
                    self.crear_db()
                    self.tabla_armazon()
                    self.dato=[(self.clave4,self.armazon.get(),self.piezas.get())]
                    self.cursor.executemany("INSERT INTO Armazones VALUES(?,?,?)",self.dato)
                    self.cerrar_db()
                    self.n=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t 3pi04")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadroarmazon.focus_set()               
    def mica(self):
        if(self.micas.get()==""):
            error2=messagebox.showwarning("Advertencia","Ingresa el nombre del articulo")
            self.Cuadromicas.focus_set()                              
        else:
            if(self.micas.get()=="cr39" or self.micas.get()=="Cr39"):
                self.clave5="cr3901"
                if(self.micas.get()=="" or self.piezas2.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()
                else:
                    self.crear_db()
                    self.tabla_micas()
                    self.dat=[(self.clave5,self.micas.get(),self.piezas2.get())]
                    self.cursor.executemany("INSERT INTO Micas VALUES(?,?,?)",self.dat)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t cr3901")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()
            if(self.micas.get()=="policarbonato" or self.micas.get()=="Policarbonato"):
                    self.clave6="polica02"
                    if(self.micas.get()=="" or self.piezas2.get()==0):
                        self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                        self.Cuadromicas.delete(0,END)
                        self.Cuadromicas.focus_set()
                    else:
                        self.crear_db()
                        self.tabla_micas()
                        self.dat=[(self.clave6,self.micas.get(),self.piezas2.get())]
                        self.cursor.executemany("INSERT INTO Micas VALUES(?,?,?)",self.dat)
                        self.cerrar_db()
                        self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t polica02")
                        self.Cuadromicas.delete(0,END)
                        self.Cuadromicas.focus_set()          
            if(self.micas.get()=="hindex" or self.micas.get()=="Hindex"):
                self.clave7="hin03"
                if(self.micas.get()=="" or self.piezas2.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()
                else:
                    self.crear_db()
                    self.tabla_micas()
                    self.dat=[(self.clave7,self.micas.get(),self.piezas2.get())]
                    self.cursor.executemany("INSERT INTO Micas VALUES(?,?,?)",self.dat)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t hin03")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()             
            if(self.micas.get()=="flat top" or self.micas.get()=="Flat top" or self.micas.get()=="Flat Top" or self.micas.get()=="flat Top"):
                self.clave8="flat04"
                if(self.micas.get()=="" or self.piezas2.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()
                else:
                    self.crear_db()
                    self.tabla_micas()
                    self.dat=[(self.clave8,self.micas.get(),self.piezas2.get())]
                    self.cursor.executemany("INSERT INTO Micas VALUES(?,?,?)",self.dat)
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso")
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t flat04")                
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()              
            if(self.micas.get()=="progresivo" or self.micas.get()=="Progresivo"):
                self.clave9="prog05"
                if(self.micas.get()=="" or self.piezas2.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()
                else:
                    self.crear_db()
                    self.tabla_micas()
                    self.dat=[(self.clave9,self.micas.get(),self.piezas2.get())]
                    self.cursor.executemany("INSERT INTO Micas VALUES(?,?,?)",self.dat)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t prog05")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadromicas.focus_set()           
    def lentes(self):
        if(self.lentes_contact.get()==""):
            mensaje=messagebox.showwarning("Error","Ingresa el nombre del articulo")
            self.Cuadrolentes.focus_set()
        else:
            if(self.lentes_contact.get()=="esferico" or self.lentes_contact.get()=="Esferico"):
                self.clave10="esf01"
                if(self.lentes_contact.get()=="" or self.piezas3.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de lente de contacto y las piezas")
                    self.Cuadrolentes.delete(0,END)
                    self.Cuadrolentes.focus_set()
                else:
                    self.crear_db()
                    self.tabla_lentes_contacto()
                    self.da=[(self.clave10,self.lentes_contact.get(),self.piezas3.get())]
                    self.cursor.executemany("INSERT INTO Lentes_contacto VALUES(?,?,?)",self.da)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n La clave del articulo es:\t esf01")
                    self.Cuadrolentes.delete(0,END)
                    self.Cuadrolentes.focus_set()                
            if(self.lentes_contact.get()=="torico" or self.lentes_contact.get()=="Torico"):
                self.clave11="tiri02"
                if(self.lentes_contact.get()=="" or self.piezas3.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de lente de contacto y las piezas")
                    self.Cuadrolentes.delete(0,END)
                    self.Cuadrolentes.focus_set()
                else:
                    self.crear_db()
                    self.tabla_lentes_contacto()
                    self.da=[(self.clave11,self.lentes_contact.get(),self.piezas3.get())]
                    self.cursor.executemany("INSERT INTO Lentes_contacto VALUES(?,?,?)",self.da)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n La clave del articulo es:\t tiri02")
                    self.Cuadrolentes.delete(0,END)
                    self.Cuadrolentes.focus_set()                
    def estuches(self):
        if(self.estuche.get()==""):
            mensaje2=messagebox.showwarning("Error","Ingresa el nombre del articulo")
            self.Cuadroestuches.focus_set()
        else:
            if(self.estuche.get()=="duro" or self.estuche.get()=="Duro"):
                self.clave12="dur01"
                if(self.estuche.get()=="" or self.piezas4.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroestuches.delete(0,END)
                    self.Cuadroestuches.focus_set()
                else:
                    self.crear_db()
                    self.tabla_estuches()
                    self.d=[(self.clave12,self.estuche.get(),self.piezas4.get())]
                    self.cursor.executemany("INSERT INTO Estuches VALUES(?,?,?)",self.d)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar\n la clave de tu articulo es:\t dur01")
                    self.Cuadroestuches.delete(0,END)
                    self.Cuadroestuches.focus_set()
            if(self.estuche.get()=="fleje" or self.estuche.get()=="Fleje"):
                self.clave13="flej02"
                if(self.estuche.get()=="" or self.piezas4.get()==0):
                    self.n1=messagebox.showinfo("Error","Ingresa el tipo de armazon y las piezas")
                    self.Cuadroestuches.delete(0,END)
                    self.Cuadroestuches.focus_set()
                else:
                    self.crear_db()
                    self.tabla_estuches()
                    self.d=[(self.clave13,self.estuche.get(),self.piezas4.get())]
                    self.cursor.executemany("INSERT INTO Estuches VALUES(?,?,?)",self.d)
                    self.cerrar_db()
                    self.e=messagebox.showinfo("Felicitaciones","Registro exitoso\n Ahora solo puedes actualizar \n la clave de tu articulo es:\t flej02")
                    self.Cuadroestuches.delete(0,END)
                    self.Cuadroestuches.focus_set()
    def actualizarmazon(self):
        if(self.clave.get()==""):
            error4=messageebox.showwarning("Error","Ingresa la Clave del articulo")
            self.Cuadroclave.focus_set()
        else:
            if(self.clave.get()=="meta01"):
                if(self.piezas.get()==0):
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadropiezas.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=?''',(self.piezas.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadroclave.delete(0,END)
            if(self.clave.get()=="past02"):
                if(self.piezas.get()==0):
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadropiezas.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=?''',(self.piezas.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadroclave.delete(0,END) 
            if(self.clave.get()=="ran03"):
                if(self.piezas.get()==0):
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadropiezas.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=?''',(self.piezas.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")               
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadroclave.delete(0,END)
            if(self.clave.get()=="3pi04"):
                if(self.piezas.get()==0):
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadropiezas.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Armazones SET  Piezas=? WHERE Clave=?''',(self.piezas.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa") 
                    self.Cuadroarmazon.delete(0,END)
                    self.Cuadropiezas.delete(0,END)
                    self.Cuadroclave.delete(0,END)
    def actualizarmica(self):
        if(self.clave.get()==""):
            mensa=messagebox.showinfo("Error","Ingresa la clave")
            self.Cuadroclave.focus_set()
        else:
            if(self.clave.get()=="cr3901"):
                if(self.piezas2.get()==0):
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadropiezas2.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas2.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadroclave.delete(0,END)
            if(self.clave.get()=="polica02"):
                if(self.piezas2.get()==0):
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadropiezas2.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas2.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadroclave.delete(0,END)                
            if(self.clave.get()=="hin03"):
                if(self.piezas2.get()==0):
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadropiezas2.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas2.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadroclave.delete(0,END)   
            if(self.clave.get()=="flat04"):
                if(self.piezas2.get()==0):
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadropiezas2.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas2.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadroclave.delete(0,END)  
            if(self.clave.get()=="prog05"):
                if(self.piezas2.get()==0):
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadropiezas2.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas2.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas2.delete(0,END)
                    self.Cuadroclave.delete(0,END)
    def actualizarlentes(self):
        if(self.clave.get()==""):
            mensa=messagebox.showinfo("Error","Ingresa la clave")
            self.Cuadroclave.focus_set()
        else:
            if(self.clave.get()=="esf01"):
                if(self.piezas3.get()==0):
                    self.Cuadropiezas3.delete(0,END)
                    self.Cuadropiezas3.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas3.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas3.delete(0,END)
                    self.Cuadroclave3.delete(0,END)
            if(self.clave.get()=="tiri02"):
                if(self.piezas3.get()==0):
                    self.Cuadropiezas3.delete(0,END)
                    self.Cuadropiezas3.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas3.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas3.delete(0,END)
                    self.Cuadroclave3.delete(0,END)                
    def actualizarestuches(self):
        if(self.clave.get()==""):
            self.mensa=messagebox.showinfo("Error","Ingresa la clave")
            self.Cuadroclave.focus_set()
        else:
            if(self.clave.get()=="dur01"):
                if(self.piezas4.get()==0):
                    self.Cuadropiezas4.delete(0,END)
                    self.Cuadropiezas4.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas4.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas4.delete(0,END)
                    self.Cuadroclave4.delete(0,END)
            if(self.clave.get()=="flej02"):
                if(self.piezas4.get()==0):
                    self.Cuadropiezas4.delete(0,END)
                    self.Cuadropiezas4.focus_set()
                else:
                    self.crear_db()
                    self.cursor.execute('''UPDATE Micas SET  Piezas=? WHERE Clave=?''',(self.piezas4.get(),self.clave.get()))
                    self.cerrar_db()
                    self.mensaje=messagebox.showinfo("Felicitaciones","Actualización exitosa")
                    self.Cuadromicas.delete(0,END)
                    self.Cuadropiezas4.delete(0,END)
                    self.Cuadroclave4.delete(0,END)    
#__________________________________________________________________OBJETO*****CONSULTA**ALMACEN__________________________________________________________________
class Calmacen(Parametros):
    def __init__(self):
        Parametros.__init__(self)
        self.raiz7=Tk()
        self.raiz7.title("Consulta Almacen Xólotl")
        self.raiz7.resizable(self.largo,self.ancho)
        self.raiz7.iconbitmap(self.direccion_ico)
        self.frame7=Frame(self.raiz7,width="900",height="500")
        self.frame7.pack()
        self.clarmazon=StringVar()
        self.clamic=StringVar()
        self.clalen=StringVar()
        self.clastuch=StringVar()
        self.clarmazon.set("")
        self.clamic.set("")
        self.clalen.set("")
        self.clastuch.set("")
        self.frame7.config(bg="LightGoldenrod1")
        self.labelclarmazon=Label(self.frame7,text="Clave Armazon:",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=5)
        self.Cuadroarmazon=ttk.Entry(self.frame7,textvariable=self.clarmazon,font=self.fuente,width=25)
        self.labelclamica=Label(self.frame7,text="Clave Mica:",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=55)
        self.Cuadromica=ttk.Entry(self.frame7,textvariable=self.clamic,font=self.fuente,width=25)
        self.labelente=Label(self.frame7,text="Clave Lentes de contacto:",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=105)
        self.Cuadrolente=ttk.Entry(self.frame7,textvariable=self.clalen,font=self.fuente,width=25)
        self.labelclastuche=Label(self.frame7,text="Clave Estuches:",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=155)
        self.Cuadroestuche=ttk.Entry(self.frame7,textvariable=self.clastuch,width=25,font=self.fuente)
        self.labelvista1=Label(self.frame7,text="Clave:",bg="LightGoldenrod1",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=255)
        self.labelvista2=Label(self.frame7,text="Articulo:",bg="LightGoldenrod1",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=305)
        self.labelvista3=Label(self.frame7,text="Piezas:",bg="LightGoldenrod1",fg="RoyalBlue1",font=(self.fuentee,self.tamaño_letra)).place(x=5,y=355)
        self.Consultarmazon=Button(self.frame7,text="Consultar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.micasc).place(x=590,y=55)
        self.Consultamica=Button(self.frame7,text="Consultar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.armazonc).place(x=590,y=5)
        self.Consultalentes=Button(self.frame7,text="Consultar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.lentesc).place(x=590,y=105)
        self.Consultaestuche=Button(self.frame7,text="Consultar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.estuchesc).place(x=590,y=155)
        self.Salir3=Button(self.frame7,text="Salir",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.raiz7.destroy).place(x=250,y=405)
        self.Regresar1=Button(self.frame7,text="Regresar",font=(self.fuentebot,self.ta_letrabut),fg="red",command=self.volver4).place(x=130,y=405)
        self.Cuadroarmazon.place(x=185,y=5)
        self.Cuadromica.place(x=140,y=55)
        self.Cuadrolente.place(x=295,y=105)
        self.Cuadroestuche.place(x=185,y=155)
        self.Cuadroarmazon.focus_set()
        self.raiz7.mainloop()
    def volver4(self): 
        self.raiz7.destroy()
        op=Menu()
    def armazonc(self):
        if(self.clarmazon.get()=="" or self.clarmazon.get()==0 ):
            self.mensajeerror=messagebox.showinfo("Error","Ingresa la clave del producto que deseas buscar")
            self.Cuadroarmazon.delete(0,END)
            self.Cuadroarmazon.focus_set()
        else:
            self.crear_db()
            self.c=[(self.clarmazon.get())]
            self.cursor.execute("SELECT * FROM  Armazones WHERE  Clave=?",self.c)
            for armazon in self.cursor:
                vis=armazon[0]
                vis2=armazon[1]
                vis3=armazon[2]
                vislabel=Label(self.frame7,text=vis,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=105,y=255)
                vislabel2=Label(self.frame7,text=vis2,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=120,y=305)
                vislabel3=Label(self.frame7,text=vis3,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=110,y=355)
            self.conexion.close()
            self.Cuadroarmazon.delete(0,END)
            self.Cuadroarmazon.focus_set()
    def micasc(self):
        if(self.clamic.get()=="" or self.clamic.get()==0):
            self.mensajeerror=messagebox.showinfo("Error","Ingresa la clave del producto que deseas buscar")
            self.Cuadromica.delete(0,END)
            self.Cuadromica.focus_set()            
        else:
            self.crear_db()
            self.consulta=[(self.clamic.get())]
            self.cursor.execute("SELECT * FROM  Micas WHERE Clave=?",self.consulta)
            for micas in self.cursor:
                vist=micas[0]
                vist2=micas[1]
                vist3=micas[2]
                vislabel=Label(self.frame7,text=vist,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=105,y=255)
                vislabel2=Label(self.frame7,text=vist2,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=120,y=305)
                vislabel3=Label(self.frame7,text=vist3,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=110,y=355)
            self.conexion.close()
            self.Cuadromica.delete(0,END)
            self.Cuadromica.focus_set()  
    def lentesc(self):
        if(self.clalen.get()=="" or self.clalen.get()==0):
            self.mensajeerror=messagebox.showinfo("Error","Ingresa la clave del producto que deseas buscar")
            self.Cuadrolente.delete(0,END)
            self.Cuadrolente.focus_set()
        else:
            self.crear_db()
            self.con=[(self.clalen.get())]
            self.cursor.execute("SELECT * FROM  Lentes_contacto WHERE Clave=?",self.con)
            for lentes in self.cursor:
                vis=lentes[0]
                vis2=lentes[1]
                vis3=lentes[2]
                vislabel=Label(self.frame7,text=vis,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=105,y=255)
                vislabel2=Label(self.frame7,text=vis2,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=120,y=305)
                vislabel3=Label(self.frame7,text=vis3,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=110,y=355)
            self.conexion.close()
            self.Cuadrolente.delete(0,END)
            self.Cuadrolente.focus_set()
    def estuchesc(self):
        if(self.clastuch.get()=="" or self.clastuch.get()==0):
            self.mensajeerror=messagebox.showinfo("Error","Ingresa la clave del producto que deseas buscar")
            self.Cuadroestuche.delete(0,END)
            self.Cuadroestuche.focus_set()
        else:
            self.crear_db()
            self.co=[(self.clastuch.get())]
            self.cursor.execute("SELECT * FROM  Estuches WHERE Clave=?",self.co)
            for estuches in self.cursor:
                vis=estuches[0]
                vis2=estuches[1]
                vis3=estuches[2]
                vislabel=Label(self.frame7,text=vis,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=105,y=255)
                vislabel2=Label(self.frame7,text=vis2,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=120,y=305)
                vislabel3=Label(self.frame7,text=vis3,bg="LightGoldenrod1",fg="Purple",width=20,font=(self.fuentee,self.tamaño_letra)).place(x=110,y=355)
            self.conexion.close()        
            self.Cuadroestuche.delete(0,END)
            self.Cuadroestuche.focus_set()
#finalmente ponemos en marcha el objeto aplicacion 
m=Aplicacion()