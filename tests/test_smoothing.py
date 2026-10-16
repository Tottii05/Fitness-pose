import pytest
from core.smoothing import EMA


def test_suaviza_poco_a_poco():
    f = EMA(0.5)
    assert f.update(10) == pytest.approx(10)
    assert f.update(20) == pytest.approx(15)
    assert f.update(20) == pytest.approx(17.5)

def test_none_devuelve_valor_anterior():
    f = EMA(0.5)
    f.update(10)
    assert f.update(None) == pytest.approx(10)

def test_none_al_principio_devuelve_none():
    f = EMA(0.5)
    assert f.update(None) is None