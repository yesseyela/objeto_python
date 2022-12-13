#Clase usuario y constructor
class Usuario:
  def __init__(self, nombre, apellido, cedula, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.edad = edad

#Clase cuenta, hereda datos de usuario. datos propios: cantidad_ahorrada
class Cuenta(Usuario):
  def __init__(self, nombre, apellido, cedula, edad, cantidad_ahorrada):
    super().__init__(nombre, apellido, cedula, edad) #this is lo de usuario
    self.cantidad_ahorrada = cantidad_ahorrada #this is propio

  def set_cantidad_ahorrada(self, cantidad): #estas son funciones sisa que devlin es self, pero se supone que va
    self.cantidad_ahorrada = cantidad #envia el valor de la cantidad

  def get_cantidad_ahorrada(self):#pide la cantidad
    return self.cantidad_ahorrada

  def mostrar(self): #como string pero largo
    print(f'Nombre: {self.nombre} {self.apellido}')
    print(f'Cédula: {self.cedula}')
    print(f'Edad: {self.edad}')
    print(f'Cantidad ahorrada: {self.cantidad_ahorrada}')

  def ingresar(self, cantidad): #pa que entre la cantidad a ingresar
    if cantidad < 0:
      print('No se puede ingresar una cantidad negativa')
    else:
      self.cantidad_ahorrada += cantidad

  def retirar(self, cantidad): #pa que entre la cantidad a retirar
    if cantidad < 0:
      print('No se puede retirar una cantidad negativa')
    else:
      self.cantidad_ahorrada -= cantidad

class Beneficio(Cuenta): #clase que trae info de cuenta pa validar datos del usuario a ver si le dan intereses segun la edad
  def __init__(self, usuario, cantidad):
    super().__init__(usuario, cantidad) #trae usuario y cantidad
    
  def es_joven(self): #compara la edad pa segun eso cambiar la cantidad -----------falta
    if self.edad >= 18 and self.edad < 28:
      return True
    else:
      return False




