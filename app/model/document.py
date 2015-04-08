__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = "sonhuytran@gmail.com"
__doc__ = ''
__version__ = '1.0'

from gi.repository import GObject


__PROP_ID__ = "id"
__PROP_NAME__ = "name"
__PROP_PATH__ = "path"
__PROP_PORT__ = "port"


class Document(GObject.GObject):
    """
    Represents a documentation, which has an UUID, a name, a path and a default server port.
    """
    # TODO: Validation

    __gsignals__ = {
        # 'my_signal': (GObject.SIGNAL_RUN_FIRST, None,
        # (int,))
    }

    id = GObject.property(type=GObject.TYPE_PYOBJECT,
                          default=None,
                          nick="Documentation id",
                          blurb="The unique id of the documentation",
                          flags=GObject.PARAM_READWRITE)

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

    def __init__(self, **properties):
        GObject.GObject.__init__(self, **properties)

    def get_id(self):
        return self.get_property(__PROP_ID__)

    def set_id(self, document_id):
        self.set_property(__PROP_ID__, document_id)

    def get_name(self):
        return self.get_property(__PROP_NAME__)

    def set_name(self, name):
        self.set_property(__PROP_NAME__, name)

    def get_path(self):
        return self.get_property(__PROP_PATH__)

    def set_path(self, path):
        self.set_property(__PROP_PATH__, path)

    def get_port(self):
        return self.get_property(__PROP_PORT__)

    def set_port(self, port):
        self.set_property(__PROP_PORT__, port)

    def serialize(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "path": self.get_path(),
            "port": self.get_port()
        }

    @staticmethod
    def deserialize(value):
        return Document(id=value["id"],
                        name=value["name"],
                        path=value["path"],
                        port=value["port"])

    @staticmethod
    def deserialize_all(values):
        return [Document.deserialize(value) for value in values]