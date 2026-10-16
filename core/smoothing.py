class EMA:
    def __init__(self, alpha=0.4):
        self.alpha = alpha
        self.x = None

    def update(self, x):
        if x is None:
            return self.x
        if self.x is None:
            self.x = x
        else:
            self.x = self.alpha * x + (1 - self.alpha) * self.x
        return self.x