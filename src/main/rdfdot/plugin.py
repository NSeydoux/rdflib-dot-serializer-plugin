from rdflib.serializer import Serializer
from rdflib.plugin import register
from rdflib import URIRef

__author__ = 'nhc'

_BEGIN = '''digraph RdflibGraph {
'''

_EDGE_TEMPLATE = '''    "{subj}" -> "{obj}" [label="{pred}"];
'''

_END = '''}
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
        stream.write(_BEGIN)
        for (s, p, o) in self.store:
            self._write_edge(stream, s, p, o)
        stream.write(_END)

    def _write_edge(self, stream, s, p, o):
        """
        Writes one line to the stream, representing the triple (s, p, o),
        if o is an rdflib.URIRef. Otherwise does nothing.
        :param stream: The output stream.
        :param s: Subject, an rdflib.URIRef
        :param p: Predicate, an rdflib.URIRef
        :param o: Object, an rdflib.URIRef or an rdflib.Literal
        :return: None
        """
        if isinstance(o, URIRef):
            stream.write(_EDGE_TEMPLATE.format(subj=self._label_for(s),
                                               pred=self._label_for(p),
                                               obj=self._label_for(o)))

    def _label_for(self, uriref):
        """
        Heuristic for providing a DOT-friendly label for an rdflib.URIRef
        occurring in self.store
        :param uriref: The URIRef to label
        :return: The label, as an rdflib.Literal or string.
        """
        assert isinstance(uriref, URIRef)
        return self.store.label(uriref, default=self.store.qname(uriref))