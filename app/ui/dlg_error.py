__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk


class ErrorDialog(Gtk.MessageDialog):
    def __init__(self, parent, *args, **kwargs):
        Gtk.MessageDialog._init(self,
                                transient_for=parent,
                                title="MkDocs Manager",
                                buttons=Gtk.ButtonsType.OK,
                                message_type=Gtk.MessageType.ERROR,
                                window_position=Gtk.WindowPosition.CENTER,
                                *args, **kwargs)