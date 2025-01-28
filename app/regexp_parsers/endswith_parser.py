
from ..nodes.base_node import BaseNode
from ..nodes.endswith_node import EndsWithNode


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    if regexp.startswith("$"):
        nodes.append(EndsWithNode())
        return regexp[1:]

    return regexp
