from ast import alias
from statistics import mode
import usuarios.usuario as modelo
import citas.acciones

class Acciones:
    def registro(self):
        print("Registro en el sistema. Introdusca los siguientes datos:")

        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        noConsultorio = input("Numero de consultorio: ")
        email = input("Email: ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, noConsultorio, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nBienvenido {registro[1].nombre} te has registrado Correctamente")
        else:
            print("\nNo te as registrado correctamente!!")

           
    def login(self):
       print("\nLOGIN: Identificate en el sistema...")
      
       try: 
           email = input("Introduce tu email: ")
           password = input("Introduce tu contraseña: ")

           usuario = modelo.Usuario('', '', '', email, password)
           login = usuario.identificar()
           if email == login[4]:
                print(f"Bienvenido {login[1]}, te has registrado en en el sistema el {6}")
                self.proximasAcciones(login)


       except Exception as e:
          """   print(type(e))
            print(type(e.__name__) """
           
          print("login incorrecto intentelo mas tarde")


    def proximasAcciones(self, usuario):
        print("""
        Aciones disponibles 
         -Agendar cita (crear)
         -Mostar citas (mostar)
         -Modificar cita (modificar)
         -Eliminar cita (eliminar)
         Salir (salir)
        """)
        accion = input("¿Que quieres hacer? ")
        hazEL = citas.acciones.Acciones()

        if accion == "crear":
            hazEL.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostar":
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "modificar":
            hazEL.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEL.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            exit()
    
    
