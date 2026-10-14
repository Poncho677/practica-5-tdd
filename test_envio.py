from envio import calcular_envio

def test_envio_estandar_3kg():
    assert calcular_envio(3, "estandar") == 50


def test_envio_estandar_mayor_que_5kg():
    assert calcular_envio(7, "estandar") == 70


def test_envio_express_3kg():
    assert calcular_envio(3, "express") == 100
