from rdfdot.plugin import DotSerializer
from rdflib import Graph
import sys

__author__ = 'nhc'

_EXAMPLE = '''#Modification of http://www.w3.org/2000/10/swap/test/meet/white.n3
     @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
     @prefix g: <http://www.another.example.org/geographical#> .
     @prefix : <http://www.example.org/meeting_organization#> .
     @prefix p: <http://www.example.org/personal_details#> .

    <http://meetings.example.com/cal#m1>     :Location  [
             g:zip "02139";
             g:lat "14.124425";
             g:long "14.245" ];
         :chair <http://www.example.org/people#fred>;
         :homePage <http://meetings.example.com/m1/hp> .

    <http://meetings.example.com/m1/hp>     :policy <http://meetings.example.com/privacyPolicy> .

    <http://www.example.org/people#fred>     :attending <http://meetings.example.com/cal#m1>;
         p:GivenName "Fred";
         p:hasEmail <mailto:fred@example.com> ;
         rdfs:label "Freddy".
'''


def main():
    DotSerializer.register()
    g = Graph()
    g.parse(format='n3', data=_EXAMPLE)
    g.serialize(destination=sys.stdout, format='dot')

if __name__ == '__main__':
    main()
