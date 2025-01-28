
from ..nodes.base_node import BaseNode
from ..nodes.startswith_node import StartsWithNode


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    if regexp.startswith("^"):
        nodes.append(StartsWithNode())
        return regexp[1:]

    return regexp
