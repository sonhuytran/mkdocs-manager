# -*- coding: utf-8 -*-

from gi.repository import Gtk

from ..model import db
from ..model.document import Document
from .win_add_doc import WinAddDocumentation
from .dlg_confirmation import ConfirmationDialog


class WinMkDocsManager(Gtk.Window):
    """
    The main window of the program, where use can CRUD & execute documentaions.
    """

    def __init__(self):
        Gtk.Window.__init__(self,
                            title="MkDocs Manager",
                            window_position=Gtk.WindowPosition.CENTER,
                            default_width=1024,
                            default_height=768)

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

        def get_name(column, cell, model, iter, data):
            cell.set_property('text', self._docs.get_value(iter, 0).get_name())

        def get_path(column, cell, model, iter, data):
            cell.set_property('text', self._docs.get_value(iter, 0).get_path())

        def get_port(column, cell, model, iter, data):
            cell.set_property('text', str(self._docs.get_value(iter, 0).get_port()))

        column_titles = ["Documentation", "Directory", "Default Port"]
        prop_funcs = [get_name, get_path, get_port]

        # Add columns to the TreeView
        for i, column_title in enumerate(column_titles):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title)
            column.pack_start(cell, True)
            column.set_cell_data_func(cell, prop_funcs[i])
            self._docs_tree.append_column(column)

        # Put the TreeView in a ScrolledWindow
        self._scrollable_docs_tree = Gtk.ScrolledWindow()
        self._scrollable_docs_tree.set_vexpand(True)
        self._scrollable_docs_tree.add(self._docs_tree)

        self._box_layout.pack_start(self._scrollable_docs_tree, True, True, 0)

        # Create a buttons box
        self._buttons_box = Gtk.ButtonBox(orientation=Gtk.Orientation.HORIZONTAL,
                                          halign=Gtk.Align.FILL)
        self._box_layout.pack_end(self._buttons_box, False, False, 0)

        # "Close" button
        self._btn_exit = Gtk.Button(label="E_xit",
                                    use_underline=True)
        self._btn_exit.connect("clicked", self._on_close)
        self._buttons_box.pack_start(self._btn_exit, False, True, 0)

        # "Add new documentation" button
        self._btn_add_doc = Gtk.Button(label="_Add new documentation",
                                       use_underline=True)
        self._btn_add_doc.connect("clicked", self._on_new_doc)
        self._buttons_box.pack_end(self._btn_add_doc, False, True, 0)

        self._load_data_to_treeview()

    def _load_data_to_treeview(self):
        self._docs.clear()
        self._docs_data = Document.deserialize_all(db.get_documents())

        for doc in self._docs_data:
            self._docs.append(None, (doc,))
            print(doc)

    def _on_new_doc(self, button):
        """
        Handle the "clicked event on the "Add new documentation" button
        """
        win_add_doc = WinAddDocumentation(self)
        win_add_doc.show_all()

    def _on_close(self, button):
        """
        Handle the "clicked" event on the "Close" button
        """
        dlg = ConfirmationDialog(parent=self,
                                 text="Exit program",
                                 secondary_text="Do you really want to exit the application?")

        if dlg.run() == Gtk.ResponseType.YES:
            self.destroy()