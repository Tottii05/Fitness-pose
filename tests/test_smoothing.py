import pytest
from core.smoothing import EMA


def test_suaviza_poco_a_poco():
    f = EMA(0.5)
    assert f.update(10) == pytest.approx(10)
    assert f.update(20) == pytest.approx(15)
    assert f.update(20) == pytest.approx(17.5)