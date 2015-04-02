__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import shelve
from os import path

from ..utils.path import APP_FOLDER
_db_file = path.join(APP_FOLDER, "mkdocs-manager.db")

mkdocs_data = shelve.open(_db_file)