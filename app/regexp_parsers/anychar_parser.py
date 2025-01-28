

from ..nodes.base_node import BaseNode
from ..nodes.anychar_node import AnyCharNode


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    if regexp[0] != ".":
        return regexp
    
    nodes.append(AnyCharNode())
    return regexp[1:]
