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

    json = jsonify(f)

    assert json == '{"b": false, "num1": 3, "num2": 2.0, "st": "hello"}'

def test_dictify_obj_with_other_primatives():
    f = Foo()
    f.num1 = 1L
    f.num2 = 3+4j
    f.null = None

    jd = dictify(f)

    assert jd['num1'] == 1L
    assert jd['num2'] == '(3+4j)'
    assert jd['null'] == None

def test_jsonify_obj_with_other_primatives():
    f = Foo()
    f.num1 = 1L
    f.num2 = 3+4j
    f.null = None

    json = jsonify(f)

    assert str(json) == '{"null": null, "num1": 1, "num2": "(3+4j)"}'

def test_dictify_obj_with_collections():
    f = Foo()
    f.li = [1,2,'three',4.0]
    f.di = {'one':1,'two':'2.0'}
    f.tu = (5,6,'seven',8.0)

    jd = dictify(f)

    assert jd['li'] == [1,2,'three',4.0]
    assert jd['di'] == {'one':1,'two':'2.0'}
    assert jd['tu'] == [5,6,'seven',8.0]

def test_jsonify_obj_with_collections():
    f = Foo()
    f.li = [1,2,'three',4.0]
    f.di = {'one':1,'two':'2.0'}
    f.tu = (5,6,'seven',8.0)

    json = jsonify(f)

    assert json == '{"li": [1, 2, "three", 4.0], "tu": [5, 6, "seven", 8.0], "di": {"two": "2.0", "one": 1}}'
