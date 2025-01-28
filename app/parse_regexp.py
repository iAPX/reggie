
"""
Parse the Regexp string and return the list of nodes generated.
Generate a IncorrectRegexpException() if the string is not a valide regexp.
"""

from .nodes.base_node import BaseNode
from .regexp_parsers import *


def parse_regexp(regexp: str, with_either: bool = True) -> list[str, list[BaseNode]]:
    nodes = []

    # Starts Node
    regexp = startswith_parser.parse(regexp, nodes)

    parsers = [
        # test_parser,
        # either_parser,
        occurences_parser,
        anychar_parser,
        endswith_parser,
        group_parser,
        sequence_parser,
        set_parser,
        literal_parser,     # Takes litteraly (in both meaning) everything not handled by the other parsers
    ]
    if with_either:
        parsers.insert(0, either_parser)

    while regexp != "":
        found = False
        for parser in parsers:
            old_regexp = regexp

            # Parsers handle the node list, to be able to manipulate it!
            regexp = parser.parse(regexp, nodes)
            if regexp != old_regexp:
                found = True
                break
        # We reached a point we could not interpret, we stop and return the result, to enable recursion
        if found == False:
            break

    return regexp, nodes
