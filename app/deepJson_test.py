from deepJson import jsonify
from deepJson import dictify

class Foo(object):
    pass

class Bar(object):
    pass

def test_dictify_obj_with_primatives():
    f = Foo()
    f.num1 = 3
    f.num2 = 2.0
    f.st = 'hello'
    f.b = False

    jd = dictify(f)

    assert jd['num1'] == 3
    assert jd['num2'] == 2.0
    assert jd['st'] == 'hello'
    assert jd['b'] == False

def test_jsonify_obj_with_primatives():
    f = Foo()
    f.num1 = 3
    f.num2 = 2.0
    f.st = 'hello'
    f.b = False

    json = dictify(f)

    assert str(json) == "{'b': False, 'num1': 3, 'num2': 2.0, 'st': 'hello'}"

def test_dictify_obj_with_other_primatives():
    f = Foo()
    f.num1 = 1L
    f.num2 = 3+4j
    f.null = None

    jd = dictify(f)

    assert jd['num1'] == 1L
    assert jd['num2'] == '(3+4j)'
    assert jd['null'] == None

def test2_jsonify_obj_with_primatives():
    f = Foo()
    f.num1 = 3
    f.num2 = 2.0
    f.st = 'hello'
    f.b = False

    json = dictify(f)

    assert str(json) == "{'b': False, 'num1': 3, 'num2': 2.0, 'st': 'hello'}"

