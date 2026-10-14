def calcular_envio(peso, tipo_envio):
    if peso <= 5 and tipo_envio == "estandar":
        return 50
    elif peso > 5 and tipo_envio == "estandar":
        return 50 + 10 * (peso - 5)
