from ClasesClientes import Clientes

def main():
    
    precio = 1000

    cliente = Clientes("Laura", "Perez", 30, 250) #Definición del cliente

    print(cliente) #__str__ method

    cliente.mostrar_cantidad_compras() # Mostrar cantidad de compras

    cliente.gastos(precio) # Calcular gastos totales

if __name__ == "__main__":
    main()