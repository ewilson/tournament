import json, types
 
def jsonify(obj):
    return json.dumps(dictify(obj))
 
def dictify(val):
    if type(val) in [int, bool, str, unicode, float, long, types.NoneType]:
        return val
    elif type(val) in [list, tuple]:
        return [dictify(item) for item in val]
    elif type(val) == dict:
        return {k: dictify(val[k]) for k in val}
    elif type(val) == complex:
        return str(val)
    else:
        return { k: dictify(getattr(val,k)) for k in val.__dict__ }
