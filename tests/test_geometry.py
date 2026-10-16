import pytest
from core.geometry import angle

def test_angulo_recto():
    assert angle((0, 1), (0, 0), (1, 0)) == pytest.approx(90)

def test_angulo_llano():
    assert angle((-1, 0), (0, 0), (1, 0)) == pytest.approx(180)

def test_angulo_cero():
    assert angle((1, 0), (0, 0), (1, 0)) == pytest.approx(0)

def test_angulo_45():
    assert angle((1, 1), (0, 0), (1, 0)) == pytest.approx(45)

def test_puntos_repetidos():
    assert angle((0, 0), (0, 0), (1, 0)) is None