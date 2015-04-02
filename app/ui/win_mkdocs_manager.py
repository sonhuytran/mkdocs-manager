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

        # The main BoxLayout of the window
        self._box_layout = Gtk.Box(spacing=5,
                                   border_width=5,
                                   orientation=Gtk.Orientation.VERTICAL)
        self.add(self._box_layout)

        # The search box Entry
        self._txt_search = Gtk.Entry(placeholder_text="Search for a documentation here")
        self._box_layout.pack_start(self._txt_search, False, True, 0)

        # The documentations TreeView
        self._docs = Gtk.TreeStore(Document.__gtype__)
        self._docs_tree = Gtk.TreeView(model=self._docs)

        # Add columns to the TreeView
        for i, column_title in enumerate(["Documentation", "Directory", "Port"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self._docs_tree.append_column(column)

        # Put the TreeView in a ScrolledWindow
        self._scrollable_docs_tree = Gtk.ScrolledWindow()
        self._scrollable_docs_tree.set_vexpand(True)
        self._scrollable_docs_tree.add(self._docs_tree)

        self._box_layout.pack_start(self._scrollable_docs_tree, True, True, 0)