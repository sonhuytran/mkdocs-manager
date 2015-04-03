__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import Gtk

from ..utils import config
from .dlg_error import ErrorDialog


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
        self._btn_doc_path.set_current_folder(config.get_last_used_doc_path())
        self._box_layout.pack_start(self._btn_doc_path, True, True, 0)

        # Buttons
        self._button_box = Gtk.HButtonBox()
        self._box_layout.pack_start(self._button_box, False, True, 0)

        # Button cancel
        self._btn_cancel = Gtk.Button(label="_Cancel",
                                      use_underline=True)
        self._btn_cancel.connect("clicked", self._on_btn_cancel_clicked)
        self._button_box.pack_start(self._btn_cancel, False, False, 0)

        # Button add doc
        self._btn_add = Gtk.Button(label="_Add",
                                   use_underline=True)
        self._btn_add.connect("clicked", self._on_btn_add_clicked)
        self._button_box.pack_end(self._btn_add, False, False, 0)

    def _on_btn_add_clicked(self, btn_add):
        document = {
            "name": self._txt_doc_name.get_text(),
            "port": self._txt_doc_port.get_text(),
            "path": self._btn_doc_path.get_current_folder()
        }

        if not document["name"]:
            dlg = ErrorDialog(parent=self,
                              text="Error: Missing Information!",
                              secondary_text="A document must have a name")
            dlg.run()
            dlg.destroy()

    def _on_btn_cancel_clicked(self, btn_cancel):
        self.destroy()