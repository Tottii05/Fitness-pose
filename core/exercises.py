from .geometry import angle
from .smoothing import EMA

class Squat:
    START_T = 150
    DEPTH_T = 100
    UP_T = 160
    SIDES = {"left": (23,25,27), "right": (24,26,28)}
    MIN_VISIBILITY = 0.6

    def __init__(self):
        self.reps = 0
        self.incomplete = 0
        self.phase = "up"
        self.started = False
        self.ema = EMA(0.4)

    def _best_side(self, lm):
        mejor_inidices = None
        mejor_vis = 0.0
        for indices in self.SIDES.values():
            vis = min(lm[i]["v"] for i in indices)
            if vis > mejor_vis:
                mejor_inidices = indices
                mejor_vis = vis
        return mejor_inidices, mejor_vis

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
        idx, vis = self._best_side(lm)
        if vis < self.MIN_VISIBILITY:
                    return {"reps" : self.reps, "incomplete" : self.incomplete, "phase" : self.phase,
                             "angle" : None, "warnings": ["Ponte de lado para que se vea mejor el cuerpo"]} 
        cadera = (lm[idx[0]]["x"] * aspect, lm[idx[0]]["y"])
        rodilla = (lm[idx[1]]["x"] * aspect, lm[idx[1]]["y"])
        tobillo = (lm[idx[2]]["x"] * aspect, lm[idx[2]]["y"])
        ang = angle(cadera, rodilla, tobillo)
        ang = self.ema.update(ang)
        if ang is not None:
            self.update_angle(ang)
        return {"reps" : self.reps, "incomplete" : self.incomplete, "phase" : self.phase, "angle" : ang, "warnings": []}