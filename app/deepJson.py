import types
import json


def jsonify(obj):
    """Converts to JSON like json.dumps, but supports objects

    Given an object or collection, jsonify will recursively iterate 
    through the fields and/or values and replace all objects with
    dictionaries using the '__dict__' attribute of each object. 
    The resulting collection is then passed into json.dumps()
    which produces a JSON representation of the input.
    """

    def _dictify(val):
        if type(val) in [int, long, float, bool, str, unicode, types.NoneType]:
            return val
        elif type(val) in [list, tuple]:
            return [_dictify(item) for item in val]
        elif type(val) == dict:
            return {k: _dictify(val[k]) for k in val}
        elif type(val) == complex:
            return {"real": val.real, "imag": val.imag}
        elif hasattr(val, '__dict__'):
            return {k: _dictify(getattr(val, k)) for k in val.__dict__}
        else:
            raise TypeError('Type %s not serializable' % type(val))

    return json.dumps(_dictify(obj))
 
