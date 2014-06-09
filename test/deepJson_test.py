from json import loads

from app.deepJson import jsonify


class Foo(object):
    def fuzz(self):
        """To show that methods don't show up in resulting JSON"""
        return "FUZZ"


class Bar(object):
    pass


def test_jsonify_obj_with_primatives():
    f = Foo()
    f.num1 = 3
    f.num2 = 2.0
    f.st = 'hello'
    f.b = False

    json = jsonify(f)

    assert loads(json) == {"b": False, "num1": 3, "num2": 2.0, "st": "hello"}


def test_jsonify_obj_with_other_primatives():
    f = Foo()
    f.num1 = 1L
    f.null = None
    f.u = u"uni"

    json = jsonify(f)

    assert loads(json) == {"null": None, "num1": 1, "u": "uni"}


def test_jsonify_obj_with_collections():
    f = Foo()
    f.li = [1, 2, 'three', 4.0]
    f.di = {'one': 1, 'two': '2.0'}
    f.tu = (5, 6, 'seven', 8.0)

    json = jsonify(f)

    assert loads(json)['li'] == [1, 2, 'three', 4.0]
    assert loads(json)['di'] == {'one': 1, 'two': '2.0'}
    assert loads(json)['tu'] == [5, 6, 'seven', 8.0]


def test__dictify_with_nested_obj():
    f = Foo()
    b = Bar()
    b.num = 3
    f.bar = b

    json = jsonify(f)

    assert loads(json) == {"bar": {"num": 3}}


def test_list():
    f = Foo()
    f.num = 1
    b = Bar()
    li = [f, b, 'three']

    json = jsonify(li)

    assert loads(json) == [{"num": 1}, {}, "three"]


def test_tuple():
    f = Foo()
    f.num = 1
    b = Bar()
    tu = (f, b, 'three')

    json = jsonify(tu)

    assert loads(json) == [{"num": 1}, {}, "three"]


def test_dict():
    f = Foo()
    f.num = 1
    b = Bar()
    di = {"foo": f, "bar": b, "three": 3.0}

    json = jsonify(di)

    assert loads(json) == {"foo": {"num": 1}, "bar": {}, "three": 3.0}


def test_primatives():
    assert "3" == jsonify(3)
    assert "3.0" == jsonify(3.0)
    assert "3" == jsonify(3L)
    assert '"three"' == jsonify("three")
    assert "false" == jsonify(False)
    assert "null" == jsonify(None)


def test_non_supported_attr():
    f = Foo()
    f.bar = 3 + 4j
    caught = False
    try:
        jsonify(f)
        assert False
    except TypeError:
        caught = True
    assert caught
