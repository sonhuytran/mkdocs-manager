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

        self._box_layout = Gtk.Box(spacing=5,
                                   border_width=5,
                                   orientation=Gtk.Orientation.VERTICAL)
        self.add(self._box_layout)

        self._documents = Gtk.TreeStore(Document.__gtype__)
        self._documents_tree = Gtk.TreeView(model=self._documents)

        for i, column_title in enumerate(["Documentation", "Directory", "Port"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self._documents_tree.append_column(column)

        #setting up the layout, putting the treeview in a scrollwindow, and the buttons in a row
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.scrollable_treelist.add(self._documents_tree)

        self._box_layout.pack_start(self.scrollable_treelist, True, True, 5)