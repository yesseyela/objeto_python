#Clase cuenta, hereda datos de usuario. datos propios: cantidad_ahorrada
from usuario import Usuario
class Cuenta(Usuario):
    def __init__(self, usuario, cantidad_ahorrada):
        self.usuario = usuario
        self.cantidad_ahorrada = cantidad_ahorrada #this is propio

    def set_cantidad_ahorrada(self, cantidad): #estas son funciones sisa que devlin es self, pero se supone que va
        if cantidad > 0:
            self.cantidad_ahorrada = cantidad #envia el valor de la cantidad
            return True
        return False

    def get_cantidad_ahorrada(self):#pide la cantidad
        return self.cantidad_ahorrada

    def mostrar(self): #como string pero largo
        presentacion = ("USUARIO-> Nombre: " + self.usuario.nombre + " Apellido: " + self.usuario.apellido + ", Edad: " + str(self.usuario.edad) + ", Cedula: " + str(self.usuario.cedula) + ", Cantidad en la cuenta: " + str(self.cantidad_ahorrada)) #Mensaje
        return presentacion

    def ingresar(self, cantidad): #pa que entre la cantidad a ingresar
        if cantidad < 0:
            print('No se puede retirar una cantidad negativa')
            return False
        else:
            self.cantidad_ahorrada += cantidad
            return True
            
    def retirar(self, cantidad): #pa que entre la cantidad a retirar
        if cantidad < 0:
            print('No se puede retirar una cantidad negativa')
            return False
        else:
            if cantidad > self.cantidad_ahorrada:
                print('Ups, no hay saldo disponible')
                return False
            else:
                self.cantidad_ahorrada -= cantidad
                return True