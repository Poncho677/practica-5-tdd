import pytest

from envio import calcular_envio

def test_envio_estandar_3kg():
    assert calcular_envio(3, "estandar") == 50


def test_envio_estandar_5kg():
    assert calcular_envio(5, "estandar") == 50
    

def test_envio_estandar_mayor_que_5kg():
    assert calcular_envio(7, "estandar") == 70


def test_envio_express_3kg():
    assert calcular_envio(3, "express") == 100


def test_envio_express_mayor_que_5kg():
    assert calcular_envio(7, "express") == 140


def test_envio_estandar_0kg():
    with pytest.raises(ValueError):
        calcular_envio(0, "estandar")


def test_envio_express_menos_2kg():
    with pytest.raises(ValueError):
        calcular_envio(-2, "express")


def test_envio_invalido_3kg():
    with pytest.raises(ValueError):
        calcular_envio(3, "urgente")
