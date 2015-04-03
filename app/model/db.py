__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import shelve
from os import path

from ..utils.path import APP_FOLDER


_db_file = path.join(APP_FOLDER, "mkdocs-manager.db")

mkdocs_data = shelve.open(_db_file, writeback=True)

_KEY_DOCUMENTS_ = "documents"


def _get_value(key, default_value):
    if key in mkdocs_data:
        return mkdocs_data[key]

    _set_value(key, default_value)
    return default_value


def _set_value(key, value):
    mkdocs_data[key] = value


def _append_value(key, value):
    if key in mkdocs_data:
        mkdocs_data[key].append(value)
    else:
        mkdocs_data[key] = [value]


def get_documents():
    return _get_value(_KEY_DOCUMENTS_, [])


def append_document(document):
    _append_value(_KEY_DOCUMENTS_, document.serialize())