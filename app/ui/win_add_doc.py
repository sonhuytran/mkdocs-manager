__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk


class WinAddDocumentation(Gtk.Window):
    def __init__(self, parent):
        Gtk.Window.__init__(self,
                            transient_for=parent,
                            modal=True,
                            title="Add a New Documentation",
                            window_position=Gtk.WindowPosition.CENTER_ON_PARENT,
                            default_width=400,
                            default_height=300)