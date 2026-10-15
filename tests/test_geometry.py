import pytest
from core.geometry import angle

def test_angulo_recto():
    assert angle((0, 1), (0, 0), (1, 0)) == pytest.approx(90)