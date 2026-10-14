from envio import calcular_envio

def test_envio_estandar_3kg():
    assert calcular_envio(3, "estandar") == 50
