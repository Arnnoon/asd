from .common_settings import *  # pylint: disable=W0401 NOSONAR


INSTALLED_APPS += [
    'accounts',
    'blogs',
]

AUTH_USER_MODEL = "accounts.User"

try:
    from configs import *  # pylint: disable=W0401 NOSONAR
except ImportError:
    pass
