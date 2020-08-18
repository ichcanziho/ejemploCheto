
class programa():
    def __init__(self,nombre):
        print("un programa vacio")
        self.nombre = nombre

    def saludar(self):
        print("hola",self.nombre)
        

p = programa('cheto')
p.saludar()

