from cuenta import Cuenta
from usuario import Usuario

class Beneficio(Cuenta): #clase que trae info de cuenta pa validar datos del usuario a ver si le dan intereses segun la edad
    def __init__(self, cuenta):
        self.cuenta = cuenta
    
    def es_joven(self): #compara la edad pa segun eso cambiar la cantidad -----------falta
        if int(self.cuenta.usuario.edad) >= 18 and int(self.cuenta.usuario.edad) < 28:
            comision = int(self.cuenta.cantidad_ahorrada) + (int(self.cuenta.cantidad_ahorrada) * 5/100)
            self.cuenta.set_cantidad_ahorrada(comision)
            return True
        else:
            return False

if __name__ == "__main__":
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cedula = input("Ingrese el número de cedula: ")
    edad = input("Ingrese su edad: ")
    usuario1 = Usuario(nombre,apellido,cedula,edad)
    cantidadXXX = input("Cantidad de la cuenta: ")

    cuenta_usu1 = Cuenta(usuario1, cantidadXXX)
    
    #print("*************GET")
    #print(cuenta_usu1.get_cantidad_ahorrada())
    #print("*************SET")
    #print(cuenta_usu1.set_cantidad_ahorrada(5000))
    #print("*************GET")
    #print(cuenta_usu1.get_cantidad_ahorrada())
    #print("*************Mostrar")
    #print(cuenta_usu1.mostrar())
    #print("*************Retirar")
    #print(cuenta_usu1.retirar(5001))
    #print("*************GET")
    #print(cuenta_usu1.get_cantidad_ahorrada())
    #print("*************Ingresar")
    #print(cuenta_usu1.ingresar(-6000))
    #print("*************GET")
    #print(cuenta_usu1.get_cantidad_ahorrada())
    prueba_beneficio = Beneficio(cuenta_usu1)
    print(prueba_beneficio.es_joven())
    print("*************GET")
    print(cuenta_usu1.get_cantidad_ahorrada())

