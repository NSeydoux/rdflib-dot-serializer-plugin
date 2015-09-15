import rdflib
__author__ = 'nhc'

_DUMMY_DOT_FILE = '''digraph MyGraph {
     a -> b -> c;
     b -> d;
 }
'''


class DotSerializer(rdflib.Serializer):
    def serialize(self, stream, base=None, encoding=None, **args):
        """
        Writes a DOT file rendering self.store to the given stream.
        :param stream: An object implementing write(str). The DOT file is written to this.
        :param base: Ignored.
        :param encoding: Ignored.
        :param args: Ignored.
        :return: None.
        """
        stream.write(_DUMMY_DOT_FILE)