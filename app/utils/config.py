__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import shelve
from os import path

from ..utils.path import APP_FOLDER


_config_file = path.join(APP_FOLDER, "mkdocs-manager.conf")
mkdocs_config = shelve.open(_config_file)

_KEY_LAST_USED_DOC_PATH = "last_use_doc_path"


def _get_value(key, default_value):
    if key in mkdocs_config:
        return mkdocs_config[key]

    return default_value


def _set_value(key, value):
    mkdocs_config[key] = value


def get_last_used_doc_path():
    return _get_value(_KEY_LAST_USED_DOC_PATH, path.expanduser('~'))


def set_last_used_doc_path(doc_path):
    _set_value(_KEY_LAST_USED_DOC_PATH, doc_path)