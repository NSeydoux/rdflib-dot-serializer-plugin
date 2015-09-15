# rdflib-dot-serializer-plugin
Render semantic web graphs using Graphviz or compatible tools.

This is an open-source plugin for rdflib that allows an rdflib.Graph() to be serialized in the DOT language, see https://en.wikipedia.org/wiki/DOT_(graph_description_language)

Usage example:
```
def main():
    DotSerializer.register()
    g = Graph()
    g.parse(format='n3', data=_EXAMPLE)
    g.serialize(destination=sys.stdout, format='dot')
```
