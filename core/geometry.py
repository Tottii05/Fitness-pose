import math 

def angle(a,b,c):
    v1 = (a[0] - b[0], a[1] - b[1])
    v2 = (c[0] - b[0], c[1] - b[1])
    largo1 = math.hypot(v1[0], v1[1])
    largo2 = math.hypot(v2[0], v2[1])
    if largo1 == 0 or largo2 == 0:
        return None
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    cos = dot / (largo1 * largo2)
    cos = max(-1.0, min(1.0, cos))
    return math.degrees(math.acos(cos))