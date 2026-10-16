class Squat:
    START_T = 150
    DEPTH_T = 100
    UP_T = 160

    def __init__(self):
        self.reps = 0
        self.incomplete = 0
        self.phase = "up"
        self.started = False

    def update_angle(self, ang):
        if self.phase == "down":
            if ang > self.UP_T:
                self.reps += 1
                self.phase = "up"
        elif self.phase == "up":
            if ang < self.DEPTH_T:
                self.phase = "down"