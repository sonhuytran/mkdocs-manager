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
                            default_width=800,
                            default_height=600)

        # main layout of the window
        self._box_layout = Gtk.Box(spacing=8,
                                   border_width=5,
                                   orientation=Gtk.Orientation.VERTICAL,
                                   hexpand=True)
        self.add(self._box_layout)

        # documentation name Entry
        self._txt_doc_name = Gtk.Entry(placeholder_text="Documentation name")
        self._box_layout.pack_start(self._txt_doc_name, False, True, 0)

        # documentation port Entry
        self._txt_doc_port = Gtk.Entry(placeholder_text="Documentation port")
        self._box_layout.pack_start(self._txt_doc_port, False, True, 0)

        # documentation path Chooser
        self._box_layout.pack_start(Gtk.Label(label="Select documentation root folder",
                                              halign=Gtk.Align.START),
                                    False, False, 0)
        self._btn_doc_path = Gtk.FileChooserWidget(action=Gtk.FileChooserAction.SELECT_FOLDER)
        self._box_layout.pack_start(self._btn_doc_path, True, True, 0)