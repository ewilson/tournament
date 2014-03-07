from deepJson import jsonify
from deepJson import dictify

class Foo(object):
    pass

class Bar(object):
    pass

def test_jsonify_obj_with_primatives():
    f = Foo()
    f.num1 = 3
    f.num2 = 2.0
    f.st = 'hello'
    f.b = False

    jd = dictify(f)
    json = jsonify(f)

    assert jd == {"b": False, "num1": 3, "num2": 2.0, "st": "hello"}
    assert json == '{"b": false, "num1": 3, "num2": 2.0, "st": "hello"}'

def test_jsonify_obj_with_other_primatives():
    f = Foo()
    f.num1 = 1L
    f.num2 = 3+4j
    f.null = None

    jd = dictify(f)
    json = jsonify(f)

    assert jd == {"null": None, "num1": 1, "num2": "(3+4j)"}
    assert json == '{"null": null, "num1": 1, "num2": "(3+4j)"}'


def test_jsonify_obj_with_collections():
    f = Foo()
    f.li = [1,2,'three',4.0]
    f.di = {'one':1,'two':'2.0'}
    f.tu = (5,6,'seven',8.0)

    jd = dictify(f)
    json = jsonify(f)

    assert jd['li'] == [1,2,'three',4.0]
    assert jd['di'] == {'one':1,'two':'2.0'}
    assert jd['tu'] == [5,6,'seven',8.0]
    assert json == '{"li": [1, 2, "three", 4.0], "tu": [5, 6, "seven", 8.0], "di": {"two": "2.0", "one": 1}}'

def test_dictify_with_nested_obj():
    f = Foo()
    b = Bar()
    b.num = 3
    f.bar = b

    jd = dictify(f)
    json = jsonify(f)

    assert jd == {"bar": {"num": 3}}
    assert json == '{"bar": {"num": 3}}'

def test_list():
    f = Foo()
    f.num = 1
    b = Bar()
    li = [f,b,'three']

    jd = dictify(li)
    json = jsonify(li)

    assert jd == [{"num": 1}, {}, "three"]
    assert json == '[{"num": 1}, {}, "three"]'

def test_tuple():
    f = Foo()
    f.num = 1
    b = Bar()
    tu = (f,b,'three')

    jd = dictify(tu)
    json = jsonify(tu)

    assert jd == [{"num": 1}, {}, "three"]
    assert json == '[{"num": 1}, {}, "three"]'

def test_dict():
    f = Foo()
    f.num = 1
    b = Bar()
    di = {"foo":f, "bar":b, "three": 3.0}

    jd = dictify(di)
    json = jsonify(di)

    assert jd == {"foo": {"num": 1}, "bar": {}, "three": 3.0}
    assert json == '{"foo": {"num": 1}, "bar": {}, "three": 3.0}'

def test_primatives():
    assert "3" == jsonify(3)
    assert "3.0" == jsonify(3.0)
    assert "3" == jsonify(3L)
    assert '"three"' == jsonify("three")
    assert "false" == jsonify(False)
    assert "null" == jsonify(None)
    assert '"3j"' == jsonify(3j)
    assert '"(2-3j)"' == jsonify(2-3j)
