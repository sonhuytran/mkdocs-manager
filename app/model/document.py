__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import GObject


class Document(GObject.GObject):
    """
    Represents a documentation, which has an UUID, a name, a path and a default server port.
    """

    __gsignals__ = {
        # 'my_signal': (GObject.SIGNAL_RUN_FIRST, None,
        # (int,))
    }

    name = GObject.property(type=GObject.TYPE_STRING,
                            default="",
                            nick="Documentation name",
                            blurb="The name of the documentation",
                            flags=GObject.PARAM_READWRITE)

    path = GObject.property(type=GObject.TYPE_STRING,
                            default="",
                            nick="Documentation path",
                            blurb="The absolute path of the directory "
                                  "containing the documentation's content",
                            flags=GObject.PARAM_READWRITE)

    port = GObject.property(type=GObject.TYPE_INT64,
                            default=1881,
                            nick="Documentation default port",
                            blurb="The default port listened by the web server "
                                  "when launching this doc",
                            flags=GObject.PARAM_READWRITE)

    def __init__(self):
        GObject.GObject.__init__(self)