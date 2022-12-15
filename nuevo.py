class Usuario:
  def __init__(self, nombre, apellido, cedula, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.edad = edad
  
  def mostrar_Usuario(self):
    txt="El usuario con nombre: {0} {1}- Con cedula: {2} - Con edad: {3}"
    return txt.format(self.nombre, self.apellido, self.cedula, self.edad)
  
  def datos(self):
    print(self.mostrar_Usuario())

class Cuenta(Usuario):
  def __init__(self,nombre, apellido, cedula, edad,cantidad):
    super().__init__(nombre, apellido, cedula, edad)
    self.cantidad = cantidad

  def datos(self):
    super().datos()
    print("Cantidad en la cuenta: {0}".format(self.cantidad))
##3##
  def set_cantidad_ahorrada(self, cantidad): #estas son funciones sisa que devlin es self, pero se supone que va
    if cantidad > 0:
            self.cantidad_ahorrada = cantidad #envia el valor de la cantidad
            return True
    return False

  def get_cantidad_ahorrada(self):#pide la cantidad
    return self.cantidad_ahorrada

  def ingresar(self, cantidad): #pa que entre la cantidad a ingresar
    if cantidad < 0:
      print('No se puede ingresar una cantidad negativa')
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

class Beneficio(Cuenta): #clase que trae info de cuenta pa validar datos del usuario a ver si le dan intereses segun la edad
  def __init__(self, usuario, cantidad):
    super().__init__(usuario, cantidad) #trae usuario y cantidad
    
  def es_joven(self): #compara la edad pa segun eso cambiar la cantidad -----------falta
        if int(self.cuenta.usuario.edad) >= 18 and int(self.cuenta.usuario.edad) < 28:
            comision = int(self.cuenta.cantidad_ahorrada) + (int(self.cuenta.cantidad_ahorrada) * 5/100)
            self.cuenta.set_cantidad_ahorrada(comision)
            return True
        else:
            return False
        
Cuenta1=Cuenta("Luisa","Yela","11","16","20000")
#print(Cuenta1.mostrar_Usuario())
Cuenta1.datos()
          