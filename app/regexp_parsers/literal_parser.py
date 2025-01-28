

from ..nodes.base_node import BaseNode
from ..nodes.literal_node import LiteralNode


"""
Parse any character or string *NOT* covered by the other parser.
Should be in the end of the list of parsers!
"""


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    chars = regexp[0]

    # These characters are prohibited
    if chars in [")", "|"]:
        return regexp
    
    if chars == "\\":
        chars = regexp[:2]
        regexp = regexp[2:]
    else:
        regexp = regexp[1:]

    if len(nodes) > 0 and isinstance(nodes[-1], LiteralNode):
        print("Add char to literal node")
        nodes[-1].add_char(chars)
    else:
        print("Add Literal Node")
        nodes.append(LiteralNode(chars))
    return regexp
