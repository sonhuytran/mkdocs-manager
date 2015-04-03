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

    __gproperties__ = {
        "name": (
            GObject.TYPE_STRING,  # type
            "Documentation name",  # nick
            "The name of the documetation",  # blurb
            "",  # default
            GObject.PARAM_READWRITE  # flags
        ),
        "path": (
            GObject.TYPE_STRING,  # type
            "Documentation path",  # nick
            "The absolute path of the directory contains the documentation's content",  # blurb
            "",  # default
            GObject.PARAM_READWRITE  # flags
        ),
        "port": (
            GObject.TYPE_INT,  # type
            "Documentation port",  # nick
            "The default port listened on the web server",  # blurb
            1,  # min
            65536,  # max
            1880,  # default
            GObject.PARAM_READWRITE  # flags
        )
    }

    __gsignals__ = {
        # 'my_signal': (GObject.SIGNAL_RUN_FIRST, None,
        # (int,))
    }

    def __init__(self):
        GObject.GObject.__init__(self)

        self.name = ""
        self.path = ""
        self.port = 1881