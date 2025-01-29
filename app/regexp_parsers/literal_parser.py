

from ..nodes.base_node import BaseNode
from ..nodes.literal_node import LiteralNode


"""
Parse any character or string *NOT* covered by the other parser.
Should be in the end of the list of parsers!
"""


def parse(regexp: str, nodes: list[BaseNode]) -> str:

    def get_next_char(regexp: str) -> tuple[str, str]:
        chars = regexp[0]
        if chars == "\\":
            chars = regexp[:2]
            regexp = regexp[2:]
            if chars == "\\x":
                chars += regexp[:2]
                regexp = regexp[2:]
        else:
            regexp = regexp[1:]
        return chars, regexp

    # These characters are prohibited
    if regexp[0] in [")", "|"]:
        return regexp
    
    chars, regexp = get_next_char(regexp)

    if len(nodes) > 0 and isinstance(nodes[-1], LiteralNode):
        print("Add char to literal node")
        nodes[-1].add_char(chars)
    else:
        print("Add Literal Node")
        nodes.append(LiteralNode(chars))
    return regexp
