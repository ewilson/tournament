import json, types
 
def jsonify(obj):
    return json.dumps(dictify(obj))
 
def dictify(obj):
    return { k: _handle_value(getattr(obj,k)) for k in obj.__dict__ }
 
def _handle_value(val):
    if type(val) in [int, bool, str, float, long, types.NoneType]:
        return val
    elif type(val) == list:
        return [dictify(item) for item in val]
    elif type(val) == dict:
        return {k: dictify(val[k]) for k in val}
    elif type(val) == complex:
        return str(val)
    else:
        return dictify(val)
