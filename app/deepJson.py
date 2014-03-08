import types
import json
 
def jsonify(obj):
    """Converts objects or collections to JSON

    Given an object, list, tuple, or dict, will recursively iterate 
    through the fields, items, and values and replace all objects with
    dictionaries. The resulting collection is then passed into json.dumps()
    which produces a JSON representation of the input.
 
    Most Python types map in an obvious way to JS types. For example, both
    list and tuple will produce an array in JS, None maps to null, etc.

    The complex type is a notable exception. I have chosen the following:
        3 + 4j -> {"real":3.0, "imag":4.0}
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
        else:
            return {k: _dictify(getattr(val, k)) for k in val.__dict__}

    return json.dumps(_dictify(obj))
 
