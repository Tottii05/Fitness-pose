from core.exercises import Squat


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