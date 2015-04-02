# -*- coding: utf-8 -*-

from gi.repository import Gtk

from ..model.document import Document


class WinMkDocsManager(Gtk.Window):
    """
    The main window of the program, where use can CRUD & execute documentaions.
    """

    def __init__(self):
        Gtk.Window.__init__(self,
                            title="MkDocs Manager",
                            window_position=Gtk.WindowPosition.CENTER,
                            default_width=640,
                            default_height=480)

        self._box_layout = Gtk.Box(spacing=6)
        self.add(self._box_layout)

        self._documents = Gtk.TreeStore(Document.__gtype__)
        self._documents_tree = Gtk.TreeView(model=self._documents)

        self._box_layout.pack_start(self._documents_tree, True, True, 0)