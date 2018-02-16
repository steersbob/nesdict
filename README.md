# NesDict

[![Build Status](https://travis-ci.org/Kargathia/nesdict.svg?branch=master)](https://travis-ci.org/Kargathia/nesdict)

Intended to add easy-to-use lookup syntax to Python's builtin `dict()`, removing the need to chain `[]` operators or `.get()` calls.

Example:

```python
from nesdict import NesDict

xdata = NesDict({
    'path': {
        'to': {
            'nested': {
                'value': 'stuff',
                'thing': 'more stuff',
                'number': 42
            },
            'something': 'else'
        }
    }
})

xdata['/path/to/nested/value'] == 'stuff'

xdata.search('/path/to/nested/*') == [
    ('/path/to/nested/value', 'stuff'), 
    ('/path/to/nested/thing', 'more stuff'),
    ('/path/to/nested/number', 42)
]

xdata.values() == ['stuff', 'more stuff', 42, 'else']
```

It also supports setting new values using the same syntax:

```python
xdata['/path/less/traveled/by'] = 'all the difference'

xdata['/path'] == {
    'to': {
            'nested': {
                'value': 'stuff',
                'thing': 'more stuff',
                'number': 42
            },
            'something': 'else'
    },
    'less': {
        'traveled': {
            'by': 'all the difference'
        }
    }
}
```