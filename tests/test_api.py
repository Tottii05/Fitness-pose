import json
from core import api

def test_process_devuelve_json_con_aviso():
    api.new_session()
    lm = [{"x": 0, "y": 0, "z": 0, "v": 0.0} for _ in range(33)]
    out = api.process(json.dumps({"aspect": 1.0, "lm": lm}))
    assert isinstance(out, str)
    result = json.loads(out)
    assert result["reps"] == 0
    assert result["warnings"]