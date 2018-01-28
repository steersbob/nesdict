"""
Tests xdict.xdict.XDict
"""

import pytest
import json
from xdict import XDict


def test_magic(xdata, data):
    assert xdata == data
    # Python does not guarantee key order when calling __str__
    assert len(str(xdata)) == len(str(data))
    assert json.dumps(xdata, sort_keys=True) == json.dumps(data, sort_keys=True)
    assert len(xdata) == len(data)

    data['var'] = 'val'
    assert not xdata == data


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
