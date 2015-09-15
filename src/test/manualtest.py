from rdfdot.plugin import DotSerializer
from rdflib import Graph
import sys

__author__ = 'nhc'


def main():
    DotSerializer.register()
    Graph().serialize(destination=sys.stdout, format='dot')

if __name__ == '__main__':
    main()
