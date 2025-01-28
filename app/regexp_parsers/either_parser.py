

from ..nodes.base_node import BaseNode
from ..nodes.either_node import EitherNode
from ..exceptions import IncorrectRegexpException


"""
Parse multiple mutually exclusive options
"""


def parse(regexp: str, nodes: list[BaseNode]) -> str:

    either_nodes = [ nodes[:] ]
    while regexp.startswith("|"):
        from ..parse_regexp import parse_regexp
        regexp, sub_nodes = parse_regexp(regexp[1:], False)
        print("Reste : ", regexp)

        either_nodes.append(sub_nodes)
    
    if len(either_nodes) > 1:
        print("Copy du nouveau either node : ", either_nodes)
        nodes.clear()
        nodes.append(EitherNode(either_nodes))
        print(nodes)

    return regexp
