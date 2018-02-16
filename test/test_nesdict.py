"""
Tests nesdict.nesdict.NesDict
"""

import pytest
import json
from nesdict import NesDict


def test_magic(xdata, data):
    assert xdata != data
    assert xdata.data == data
    # Python does not guarantee key order when calling __str__
    assert len(str(xdata)) == len(str(data))
    # We can't directly serialize xdata - we need to access the underlying data
    assert json.dumps(xdata.data, sort_keys=True) == json.dumps(data, sort_keys=True)
    assert len(xdata) == len(data)


def test_get(xdata, data):
    assert xdata.get('_id') == data['_id']
    assert xdata.get('/_id') == xdata.get('_id')
    assert xdata.get('/tags/2') == data['tags'][2]
    assert xdata.get('/tags')[2] == data['tags'][2]
    assert xdata.get('nonsense') is None

    with pytest.raises(KeyError):
        xdata.get('nonsense', allow_default=False)

    with pytest.raises(TypeError):
        xdata.get()

    with pytest.raises(TypeError):
        data.get()

    with pytest.raises(ValueError):
        xdata.get('*')


def test_search(xdata, data):
    assert xdata.search('*') == data

    assert xdata.search('*id') == {
        '_id': data['_id'],
        'guid': data['guid']
    }

    assert xdata.search('**/id') == {
        'friends': [
            {'id': 0},
            {'id': 1},
            {'id': 2}
        ]
    }

    assert xdata.search('*/*/id') == {
        'friends': [
            {'id': 0},
            {'id': 1},
            {'id': 2}
        ]
    }

    assert xdata.search('**/*id') == {
        '_id': data['_id'],
        'guid': data['guid'],
        'friends': [
            {'id': 0},
            {'id': 1},
            {'id': 2}
        ]
    }

    # '.' for wildcard single is not supported
    assert xdata.search('.id') == {}
    # but '?' is
    assert xdata.search('?id') == {'_id': data['_id']}


def test_set(xdata):
    xdata.set('var', 'val')
    assert xdata.get('var') == 'val'

    with pytest.raises(TypeError):
        # We can't implicitly overwrite 'var' from str to dict
        xdata.set('/var/l/5', 5)

    # ...but we can do it explicitly
    xdata.set('/var', dict())

    # New values are assumed to be dict keys by default
    xdata.set('/var/5', 6)
    assert xdata.get('var') == {'5': 6}

    # Setting a numeric key to a list will insert just fine
    xdata.set('/var/l', ['first'])
    xdata.set('/var/l/3', 'x')
    assert xdata.get('/var/l') == ['first', None, None, 'x']

    # /var/l is a list - no string key please
    with pytest.raises(TypeError):
        xdata.set('/var/l/str')


def test_setdefault(xdata):
    xdata.setdefault('var', 'val')
    assert xdata.get('var') == 'val'

    xdata.setdefault('_id', 'val')
    assert xdata.get('_id') != 'val'

    xdata.setdefault('/vard/b/c', 'val')
    assert xdata.get('/vard/b/c') == 'val'


@pytest.mark.parametrize('key', [
    '_id',
    '/friends/0/name',
    '/tags/0',
    '*',
    '*/*',
    '???'
])
def test_contains(xdata, key):
    assert key in xdata


@pytest.mark.parametrize('key', [
    'X',
    '/*/*/*/*/?',
    '/age/*',
    '/tags/deserunt',
    '/*/gender'
])
def test_no_contains(xdata, key):
    assert key not in xdata


def test_iterate(xdata, data):
    # we also get the nested keys
    assert len(xdata.keys()) > len(data.keys())
    assert '_id' in xdata.keys()
    assert 'friends/0/id' in xdata.keys()

    # 'in xdata' equals 'in xdata.keys()'
    assert '_id' in xdata
    assert 'friends/0/id' in xdata

    # can pass custom search paths to keys()
    assert 'friends/0/id' not in xdata.keys('*')
    assert '_id' in xdata.keys('*')

    # iterate over values
    assert len(xdata.keys()) == len(xdata.values())
    assert 'aliquip' in xdata.values()
    assert 'aliquip' not in xdata.values('*')
    assert 'blue' in xdata.values('*')

    # iterate over key/value tuples
    assert len(xdata.keys()) == len(xdata.items())
    assert ('friends/2/id', 2) in xdata.items()
    assert ('friends/2/id', 2) not in xdata.items('*')
    assert ('gender', 'female') in xdata.items('*')

    # iterate over entire collection
    assert [x for x in xdata].sort() == [x for x in data].sort()


@pytest.mark.parametrize('key', [
    '_id',
    '/friends/0/name',
    '/tags/0'
])
def test_bracket_get(xdata, key):
    assert xdata[key] == xdata.get(key)


def test_bracket_set(xdata):
    xdata['var'] = {'val': 'stuff'}
    xdata['var/something'] = 'else'

    assert xdata['var'] == {'val': 'stuff', 'something': 'else'}


def test_del(xdata):
    del xdata['about']
    assert 'about' not in xdata

    del xdata['friends/0/name']
    assert 'name' not in xdata.get('friends/0')

    with pytest.raises(KeyError):
        del xdata['stuff']

    with pytest.raises(KeyError):
        del xdata['nested/stuff']


def test_copy(xdata, data):
    assert xdata.copy().__class__ == xdata.__class__


def test_nested(xdata):
    xxdata = NesDict(xdata)

    assert xxdata['friends/0/name'] == xdata['friends/0/name']
    assert xxdata.search('*') == xdata.search('*')
