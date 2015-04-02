# -*- coding: utf-8 -*-

from gi.repository import Gtk

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

        # Add columns to the TreeView
        for i, column_title in enumerate(["Documentation", "Directory", "Default Port"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
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
        self._btn_close = Gtk.Button(label="_Close",
                                     use_underline=True)
        self._btn_close.connect("clicked", self._on_close)
        self._buttons_box.pack_start(self._btn_close, False, True, 0)

        # "Add new documentation" button
        self._btn_add_doc = Gtk.Button(label="_Add new documentation",
                                       use_underline=True)
        self._btn_add_doc.connect("clicked", self._on_new_doc)
        self._buttons_box.pack_end(self._btn_add_doc, False, True, 0)

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
        dlg = ConfirmationDialog(text="MkDocs Manager",
                                 secondary_text="Do you really want to exit the application?")

        if dlg.run() == Gtk.ResponseType.YES:
            Gtk.main_quit()