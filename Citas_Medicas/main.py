from usuarios import acciones

print("""
####### BIENVENIDO #######
Acciones desponibles
  -registro
  -login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?:")

if accion == "registro":
  hazEl.registro()

elif accion == "login":
  hazEl.login()
