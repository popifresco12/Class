#Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
#Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
#La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener 
# el importe del interés (cantidad*interés/100) y otro método para mostrar la información, 
# datos del titular plazo, interés y total de interés.
#Crear al menos un objeto de cada subclase.


class cuenta:
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad
    
    def imprimir(self):
        print(self.titular)
        print(self.cantidad)
    

class cajaahorro(cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
        print("caja de ahorro")

    def mostrar(self):
        print(self.titular)
        print(self.cantidad)



class plazofijo(cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes
        print("plazo fijo")

    def calcular(self):
        self.inter=(self.cantidad * self.interes) / 100
        self.total=(self.cantidad * self.inter) * self.plazo

    def mostrar(self):
        print(self.inter)
        print(self.interes)
        print(self.plazo)
        print(self.titular)
        print(self.cantidad)
        print(self.total)

    def __del__(self):
        print("CERRANDO")
        

nom = input("Escribe el nombre de la cuenta: ")
q = int(input("Escribe la cantidad de la cuenta: "))
pla = int(input("¿Cúal es el plazo?: "))
i = int(input("¿Cúal es el interés?: "))

count=cuenta(nom,q)
count.imprimir()
caja=cajaahorro(nom, q)
caja.mostrar()
plazof=plazofijo(nom, q, pla, i)
plazof.calcular()
plazof.mostrar()

