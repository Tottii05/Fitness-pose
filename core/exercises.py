from .geometry import angle
from .smoothing import EMA

class Squat:
    START_T = 150
    DEPTH_T = 100
    UP_T = 160

    def __init__(self):
        self.reps = 0
        self.incomplete = 0
        self.phase = "up"
        self.started = False
        self.ema = EMA(0.4)

    def update_angle(self, ang):
        if self.phase == "down":
            if ang > self.UP_T:
                self.reps += 1
                self.phase = "up"
                self.started = False
        elif self.phase == "up":
            if ang < self.START_T:
                self.started = True
            if ang < self.DEPTH_T:
                self.phase = "down"
            elif self.started and ang > self.UP_T:
                self.incomplete += 1
                self.started = False

    def update(self, lm, aspect = 1.0):
        cadera = (lm[23]["x"] * aspect, lm[23]["y"])
        rodilla = (lm[25]["x"] * aspect, lm[25]["y"])
        tobillo = (lm[27]["x"] * aspect, lm[27]["y"])
        ang = angle(cadera, rodilla, tobillo)
        ang = self.ema.update(ang)
        if ang is not None:
            self.update_angle(ang)
        return {"reps" : self.reps, "incomplete" : self.incomplete, "phase" : self.phase, "angle" : ang}