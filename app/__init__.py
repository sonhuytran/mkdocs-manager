__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import sys
from gi.repository import Gtk

from .ui.win_mkdocs_manager import WinMkDocsManager
from .utils.log import getLogger


def main():
    logger = getLogger()
    logger.info("App Started")

    win = WinMkDocsManager()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    sys.exit(main())