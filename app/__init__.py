__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

import sys

from gi.repository import Gtk

from .ui.win_mkdocs_manager import WinMkDocsManager
from .utils.log import getLogger
from .utils import config
from .model import db


def main():
    logger = getLogger()
    logger.info("App Started")

    win = WinMkDocsManager()
    win.connect("delete-event", _on_window_deleted)
    win.connect("destroy", _on_window_destroyed)
    win.show_all()
    Gtk.main()

    logger.info("App Exitted")


def _on_window_deleted(widget, event):
    exit_program()


def _on_window_destroyed(widget):
    exit_program()


def exit_program():
    # Close the database
    if config.mkdocs_config is not None:
        config.mkdocs_config.close()
        config.mkdocs_config = None

    if db.mkdocs_data is not None:
        db.mkdocs_data.close()
        db.mkdocs_data = None

    # Exit the main loop
    Gtk.main_quit()


if __name__ == '__main__':
    sys.exit(main())