import sqlite3

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("5- Listado de automoviles")
            print("4- Cargar disponibilidad")
            print("3- Borrar datos del automovil")
            print("2- Modificar Automovil")
            print("1- Cargar Automovil")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
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
                Listado_Automoviles = Automovil(marca,modelo,precio,cantidadDisponibles)
                Listado_Automoviles.listado_automoviles()

                            
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
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
    
    def listado_automoviles(self): #Consigna nro5
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

    def crearTablas(self): #consigna nro6
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETA (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30) ,marca  VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATATIME, NOT UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

#quiza hay que crear otro archivo?? 
@dataclass
class Motocicleta():
    #def __init__(self, modelo, marca, precio, color, fechaUltimoPrecio):
    modelo: str
    marca: str
    precio: int
    color: str
    fechaUltimoPrecio: str
    #no se si se podrá hacer con un data class o con el contructor como arriba

    def crearTablas(self): #consigna nro7
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_MOTOCICLETA")
        conexion.miCursor.execute("CREATE TABLE HISTORICO_MOTOCICLETA (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30) ,marca  VARCHAR(30),precio INTEGER NOT NULL, color VARCHAR(30), fechaUltimoPrecio DATATIME, NOT UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()
    
    def modificar_moto(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETA SET precio=(precio*10)/100 where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
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
