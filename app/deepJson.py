import types
import json
 
def jsonify(obj):
    return json.dumps(dictify(obj))
 
def _dictify(val):
    if type(val) in [int, bool, str, unicode, float, long, types.NoneType]:
        return val
    elif type(val) in [list, tuple]:
        return [_dictify(item) for item in val]
    elif type(val) == dict:
        return {k: _dictify(val[k]) for k in val}
    elif type(val) == complex:
        return str(val)
    else:
        return { k: _dictify(getattr(val,k)) for k in val.__dict__ }
