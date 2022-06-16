import citas.cita as modelo

class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}!!! Vamos a crear una nueva cita...")

        paciente = input("Introduce el nombre del paciente: ")
        problema = input("Escribe la descripcion de la cita/consulta: ")
        horaAtencion = input("Escribe El horario de antencion: ")
        costo = input("Escribe el costo: ")
        cita = modelo.Cita(usuario[0], paciente, problema, horaAtencion, costo)
        guardar = cita.guardar()

        if guardar[0] >=1:
            print(f"\nPerfecto has Agendado la cita de {cita.paciente}")
        else:
            print(f"\nNo has guardado la cita {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\n{usuario[1]} Estas son tus citas")
        cita = modelo.Cita(usuario[0])
        citas = cita.listar()
        #print(notas)
        for cita in citas:
            print("\n***********************")
            print(cita[2])
            print(cita[3])
            print("\n***********************")
    
    def modificar(self, usuario):
            print(f"\n{usuario[1]} Editar cita ")
            print("Introduca los nuevos datos")

            Paciente = input("Introduce el nombre del paciente: ")
            Problema = input("Escribe la descripcion de la cita/consulta: ")
            HoraAtencion = input("Escribe El horario de antencion: ")
            Costo = input("Escribe el costo: ")
            cita = modelo.Cita(usuario[0], Paciente, Problema, HoraAtencion, Costo)
            modificar = cita.modificar()
            

            
    def borrar(self, usuario):
            print(f"\n{usuario[1]} !!!Estar por Borrar alguna cita !!!")

            paciente = input("Introduce el nombre del paciente ")
            cita = modelo.Cita(usuario[0], paciente)
            eliminar = cita.eliminar()
            if eliminar[0]>=1:
                print(f"Se borro")
            else:
                print("No se borro la cita, prueba mas tarde")
