__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import sys

from gi.repository import Gtk

from .ui.main import WinMkDocsManager


def main():
    win = WinMkDocsManager()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    sys.exit(main())