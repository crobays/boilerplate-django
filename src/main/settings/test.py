from base import *

MIDDLEWARE_CLASSES += (
    'mango.middleware.LoggedInMiddleware',
)

SAFE_IPS = [
    os.environ.get('SAFE_IPS', '').split(','),
    '127.0.0.1',
]
