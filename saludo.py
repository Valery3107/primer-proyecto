class saludo():

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def saludar(self):
        print(self.mensaje)

saludo = saludo("Hola Mundo")
saludo.saludar() 