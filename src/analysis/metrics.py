import numpy as np

def calculate_velocity(track):
    positions = np.array(track.history)
    if len(positions) < 2:
        return 0.0
    displacement = positions[-1] - positions[-2]
    return np.linalg.norm(displacement)

def calculate_msd(track):
    # Mean Squared Displacement
    positions = np.array(track.history)
    start = positions[0]
    return np.mean(np.sum((positions - start)**2, axis=1))
