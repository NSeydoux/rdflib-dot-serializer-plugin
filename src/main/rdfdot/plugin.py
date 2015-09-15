from rdflib.serializer import Serializer
from rdflib.plugin import register

__author__ = 'nhc'

_DUMMY_DOT_FILE = '''digraph MyGraph {
     a -> b -> c;
     b -> d;
 }
'''


class DotSerializer(Serializer):
    """
    An rdflib.Serializer that outputs a DOT file, see https://en.wikipedia.org/wiki/DOT_(graph_description_language)
    """

    @classmethod
    def register(cls):
        """
        Registers this Serializer with rdflib.
        Call this before using my_graph.serialize(format='dot')
        :return: None
        """
        register('dot', Serializer, cls.__module__, cls.__name__)

    def serialize(self, stream, base=None, encoding=None, **args):
        """
        TODO: Under construction! This is a dummy implementation.
        Writes a DOT file rendering self.store to the given stream.
        :param stream: An object implementing write(str). The DOT file is written to this.
        :param base: Ignored.
        :param encoding: Ignored.
        :param args: Ignored.
        :return: None.
        """
        stream.write(_DUMMY_DOT_FILE)