import numpy as np

class KalmanFilter:
    def __init__(self):
        self.dt = 1
        # State transition matrix
        self.A = np.array([[1, 0, self.dt, 0],
                           [0, 1, 0, self.dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        # Measurement matrix
        self.H = np.array([[1, 0, 0, 0],
                           [0, 1, 0, 0]])
                           
    def predict(self):
        # Predict state
        pass
        
    def update(self, z):
        # Update with measurement
        pass
