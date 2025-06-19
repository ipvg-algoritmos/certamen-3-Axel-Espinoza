edad = int(input("Ingresa tu edad: "))
supervisor = input("¿Eres supervisor? (s/n): ")
autorizacion = input("¿Tienes una autorizacion? (s/n): ")
while True:
    if edad < 18 or supervisor == "n" and autorizacion == "n":
        print ("Acceso denegado.")
        break
    else:
        edad >= 18 and supervisor == "s" or autorizacion == "s"
        print ("Acceso permitido.")
        break