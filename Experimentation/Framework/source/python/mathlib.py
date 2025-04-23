
import math

def distance(u: tuple[float, float], v: tuple[float, float]) -> float:
    dx = v[0] - u[0]
    dy = v[1] - u[1]
    return math.sqrt(dx * dx + dy * dy)

