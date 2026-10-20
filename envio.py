class caja:

    def __init__(self, peso, tipo):
        self.peso = peso
        self.tipo = tipo

    def obtener_incremento(self):
        if self.tipo == "estandar":
            return 10
        else:
            return 20

    def obtener_precio(self):
        if self.tipo == "estandar":
            return 50
        else:
            return 100

def calcular_envio(peso, tipo_envio):
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que 0")

    categoria = ["estandar", "express"]
    
    if tipo_envio in categoria:
        c = caja(peso, tipo_envio)
        if peso > 0 and peso <= 5:
            return c.obtener_precio()
        else:
            return (peso - 5) * c.obtener_incremento() + c.obtener_precio()
    else:
        raise ValueError("El tipo de envío solo puede ser estandar o express")
    
