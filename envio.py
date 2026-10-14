def calcular_envio(peso, tipo_envio):
    if peso == 0:
        raise ValueError("El peso debe ser diferente de 0")
    if peso <= 5 and tipo_envio == "estandar":
        return 50
    elif peso > 5 and tipo_envio == "estandar":
        return 50 + 10 * (peso - 5)
    if peso <= 5 and tipo_envio == "express":
        return 100
    elif peso > 5 and tipo_envio == "express":
        return 100 + 20 * (peso - 5)
