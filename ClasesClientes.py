
class Persona:
    def __init__(self, nombre, apellido, edad): #Magic method __init__
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self): #Magic method __str__
        return f"Cliente: {self.nombre} {self.apellido}, {self.edad} años"
    
    
class Clientes (Persona): #Definicion de la clase Clientes que hereda de Persona
    def __init__(self, nombre, apellido, edad,  cantidad_compras):
        super().__init__(nombre, apellido, edad) #Llama al constructor de la clase base Persona
        self.cantidad_compras = cantidad_compras

    def mostrar_cantidad_compras(self): # Método para mostrar la cantidad de compras
        print(f"Cantidad de compras realizadas: {self.cantidad_compras}")

    def gastos(self,precio):    # Método para calcular el total gastado
        print(f"Ha gastado un total de: {self.cantidad_compras * precio} pesos")