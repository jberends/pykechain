import requests

from kechain2.models import Part, Property

API_ROOT = 'http://0.0.0.0:8000/'

API_PATH = {
    'parts': 'api/parts.json',
    'properties': 'api/properties.json',
    'property': 'api/properties/{property_id}.json'
}

HEADERS = {
    'Authorization': 'Token 4fd189d669793373264dc188ce902a2af99d90bc'
}


def api_url(resource, **kwargs):
    return API_ROOT + API_PATH[resource].format(**kwargs)


def parts(name=None, category='INSTANCE'):
    r = requests.get(api_url('parts'), headers=HEADERS, params={
        'name': name,
        'category': category
    })

    assert r.status_code == 200, "Could not retrieve parts"

    data = r.json()

    return [Part(p) for p in data['results']]


def part(*args, **kwargs):
    _parts = parts(*args, **kwargs)

    assert len(_parts) == 1, "Multiple parts fit criteria"

    return _parts[0]


def properties(name=None, category='INSTANCE'):
    r = requests.get(api_url('properties'), headers=HEADERS, params={
        'name': name,
        'category': category
    })

    assert r.status_code == 200, "Could not retrieve properties"

    data = r.json()

    return [Property(p) for p in data['results']]
