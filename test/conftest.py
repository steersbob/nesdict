"""
conftest.py: default file for pytest fixtures
"""

import pytest
from nesdict import NesDict


@pytest.fixture
def data():
    return {
        '_id': '5a6e0b08691ccec34379375c',
        'index': 0,
        'guid': '11bd2317-53e4-4759-b9dd-2cd3eff1b51c',
        'isActive': True,
        'balance': '$3,181.39',
        'picture': 'http://placehold.it/32x32',
        'age': 32,
        'eyeColor': 'blue',
        'name': 'Polly Hess',
        'gender': 'female',
        'company': 'QUARMONY',
        'email': 'pollyhess@quarmony.com',
        'phone': '+1 (887) 449-2398',
        'address': '877 Montgomery Street, Silkworth, Minnesota, 4614',
        'about': 'Labore et adipisicing voluptate dolore excepteur veniam '
                    'commodo sint cupidatat fugiat ad quis. Esse mollit culpa '
                    'dolore deserunt dolor quis officia quis magna ex veniam consequat '
                    'aute. Sint non nisi laboris ut Lorem. Anim do cupidatat est tempor.\r\n',
        'registered': '2017-06-19T08:10:47 -02:00',
        'latitude': -10.291164,
        'longitude': 86.432741,
        'tags': [
            'deserunt',
            'labore',
            'deserunt',
            'non',
            'aliquip',
            'dolor',
            'dolore'
        ],
        'friends': [
            {
                'id': 0,
                'name': 'Alta Thompson'
            },
            {
                'id': 1,
                'name': 'Hart Ellison'
            },
            {
                'id': 2,
                'name': 'Shari Sykes'
            }
        ],
        'greeting': 'Hello, Polly Hess! You have 7 unread messages.',
        'favoriteFruit': 'apple'
    }


@pytest.fixture
def xdata(data):
    return NesDict(data)
