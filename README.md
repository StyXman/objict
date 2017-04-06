**NOTE**: This is not abandoned code, it's just that is so simple, it really
doesn't need much maintenance. Still, any issues will be treated with due
diligency.

`objict` objects behave like JavaScript objects, whose attributes can be also
accessed as dictionaty keys. That's a slightly complicated way to say:

    o = objict()
    o.a = 1
    assert o['a'] == 1
    o['b'] = 2
    assert o.b == 2

`objict`s can be created like any other `dict`, but it will convert `dict`
values into `objict`s:

    o = objict({'a': {'b': 1}})
    assert o.a.b == 1
    assert o['a'].b == 1
    assert o.a['b'] == 1
    assert o['a']['b'] == 1

This means that you can convert `json` strings to `objict`s easily. As for
`dump()`ing, due to inconsistencies betwwen the Python-based and C-based
encoders, you must do this:

    o = objict({'a': {'b': 1}})
    import json.encoder
    json.encoder.c_make_encoder = None
    assert json.dumps(o) == '{"a": {"b": 1}}'

Finally, the objects behave like any other `dict`.
