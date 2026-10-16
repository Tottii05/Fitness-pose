from core.exercises import Squat


def test_cuenta_una_repeticion():
    s = Squat()
    for ang in [170, 120, 95, 120, 155, 165]:
        s.update_angle(ang)
    assert s.reps == 1