import json 
from .exercises import Squat

_session = None

def new_session():
    global _session
    _session = Squat()

def process(payload):
    data = json.loads(payload)
    result = _session.update(data["lm"], data["aspect"])
    return json.dumps(result)