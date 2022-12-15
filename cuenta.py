class Usuario:
  def __init__(self, nombre, apellido, cedula, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.edad = edad

class Cuenta(Usuario):
  def __init__(self, nombre, apellido, cedula, edad, saldo):
    super().__init__(nombre, apellido, cedula, edad)
    self.saldo = saldo

  def setSaldo(self, saldo):
    self.saldo = saldo

  def getSaldo(self):
    return self.saldo

  def mostrar(self):
    print("Resumen del cliente:")
    print("Nombre:", self.nombre)
    print("Apellido:", self.apellido)
    print("Cédula:", self.cedula)
    print("Edad:", self.edad)
    print("Saldo:", self.saldo)

  def ingresar(self, cantidad):
    if cantidad > 0:
      self.saldo += cantidad
      print("Se ha depositado", cantidad, "en la cuenta.")
    else:
      print("No se pueden depositar cantidades negativas en la cuenta.")

  def retirar(self, cantidad):
    if cantidad > 0:
      if cantidad <= self.saldo:
        self.saldo -= cantidad
        print("Se ha retirado", cantidad, "de la cuenta.")
      else:
        print("No se puede retirar, " cantidad, "de la cuenta.")
    return self.cantidad
