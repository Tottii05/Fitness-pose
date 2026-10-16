import math
from core.exercises import Squat

def frame(theta):
    lm = [{"x": 0, "y": 0, "z": 0, "v": 0.0} for _ in range(33)]
    t = math.radians(theta)
    lm[25] = {"x": 0.5, "y": 0.6, "z": 0, "v": 0.99}                                          # rodilla
    lm[27] = {"x": 0.5, "y": 0.8, "z": 0, "v": 0.99}                                          # tobillo
    lm[23] = {"x": 0.5 + 0.2 * math.sin(t), "y": 0.6 + 0.2 * math.cos(t), "z": 0, "v": 0.99}  # cadera
    return lm

def test_cuenta_una_repeticion():
    s = Squat()
    for ang in [170, 120, 95, 120, 155, 165]:
        s.update_angle(ang)
    assert s.reps == 1

def test_media_sentadilla_es_incompleta():
    s = Squat()
    for ang in [170, 140, 120, 155, 165]:
        s.update_angle(ang)
    assert s.reps == 0
    assert s.incomplete == 1

def test_repeticion_completa_no_cuenta_incompleta():
    s = Squat()
    for ang in [170, 120, 95, 120, 155, 165, 170]:
        s.update_angle(ang)
    assert s.reps == 1
    assert s.incomplete == 0

def test_update_con_landmarks():
    s = Squat()
    for ang in [170, 95, 170]:
        for _ in range(10):
            s.update(frame(ang))
    assert s.reps == 1
    assert s.incomplete == 0