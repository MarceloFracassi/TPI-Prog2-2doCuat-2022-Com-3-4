import sqlite3
from dataclasses import dataclass

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("7- Modificar precio Motocicleta")
            print("6- Cargar Motocicleta")
            print("5- Listado de automoviles")
            print("4- Cargar disponibilidad")
            print("3- Borrar datos del automovil")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            try:
                nro = int(input("Por favor ingrese un numero"))

                if nro == 1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio = input("Por favor ingrese el precio del automovil: ")
                    cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if nro ==2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = input("Por favor ingrese el nuevo precio: ")
                    automovil_a_modificar=Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                if nro ==3:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    automovil_a_eliminar=Automovil(marca,modelo)
                    automovil_a_eliminar.delete_automoviles()
                if nro ==4:
                    disponibilidad = Automovil(marca,modelo)
                    disponibilidad.cargar_disponibilidad()
                if nro ==5:
                    print("Marca" " " "Modelo" " " "Precio" " " "Cantidad disponible")
                    Automovil.listado_automoviles()
                if nro==6: 
                    modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                    marca = input("Por favor ingrese la marca de la motocicleta: ")
                    cilindrada = input("Por favor ingrese la cilindrada de la motocicleta: ")
                    precio = input("Por favor ingrese el precio de la motocicleta: ")
                    color = input("Por favor ingrese el color de la motocicleta: ")
                    crear_tabla_motocicleta= Motocicleta(modelo, marca, cilindrada, precio, color)
                    crear_tabla_motocicleta.cargar_motocicleta()
                    crear_tabla_motocicleta.carga_historial()
                if nro ==7:
                    print("Se modifico el precio un 10%")
                    motocicleta_a_modificar= Motocicleta()
                    motocicleta_a_modificar.modificar_moto()
                if nro==0:
                    break
            except: 
                print('Por favor ingrese un numero y no una letra')
                continue     
    #TABLA DE AUTOMOVILES
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETA")                      #autoincrementa
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETA (id_moto INTEGER PRIMARY KEY AUTOINCREMENT, modelo  VARCHAR(30) , marca  VARCHAR(30), cilindrada VARCHAR(30), precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME DEFAULT CURRENT_TIMESTAMP)") 
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETA (id_moto INTEGER, modelo  VARCHAR(30) , marca  VARCHAR(30), cilindrada VARCHAR(30), precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATETIME)") 
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                                                                    
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
            input()
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
     
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
            input()
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    
    def delete_automoviles(self): #Consigna nro3
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM AUTOMOVILES  where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil eliminado correctamente")
            input()
        except:
            print('Error al eliminar un automovil')
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self): #Consigna nro4
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles+1 where marca='{}' and modelo='{}' ".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
            input()
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    
    @classmethod
    def listado_automoviles(cls): #Consigna nro5
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos=conexion.miCursor.fetchall()
            for auto in autos: 
                a,b,c,d,*rest = auto
                concatenado=f"{a} {b} {c} {d}"
                print(concatenado)
            input()
        except:     
            print('Error al ejecutar')
        finally:
            conexion.cerrarConexion()

class Motocicleta:
    def __init__(self, modelo, marca, cilindrada, precio, color):
        self.modelo = modelo
        self.marca = marca
        self.cilindrada = cilindrada
        self.precio = precio
        self.color = color

    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                                                                    
            conexion.miCursor.execute("INSERT INTO MOTOCICLETA(modelo,marca,cilindrada,precio,color) VALUES('{}','{}','{}','{}','{}')".format(self.modelo, self.marca, self.cilindrada, self.precio, self.color))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
            input()
        except:
            print("Error al agregar una motocicleta")
        finally:
            conexion.cerrarConexion()

    def carga_historial(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:                                                                                                    
            conexion.miCursor.execute("INSERT INTO HISTORICO_MOTOCICLETA(modelo,marca,cilindrada,precio,color) VALUES('{}','{}','{}','{}','{}')".format(self.modelo, self.marca, self.cilindrada, self.precio, self.color))
            conexion.miConexion.commit()
            print("Historial cargado exitosamente")
            input()
        except:
            print("Error al cargar")
        finally:
            conexion.cerrarConexion()

    def modificar_moto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETA SET precio=(precio - ((precio*10)/100))")
            conexion.miConexion.commit()
            print("Motocicleta modificado correctamente")
            input()
        except:
            print('Error al actualizar una monoticleta')
        finally:
            conexion.cerrarConexion() 

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
