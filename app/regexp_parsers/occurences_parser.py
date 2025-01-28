

from ..nodes.base_node import BaseNode
from ..nodes.occurences_node import OccurencesNode
from ..nodes.literal_node import LiteralNode
from ..exceptions import IncorrectRegexpException


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    char = regexp[0]
    if char not in ["*", "+", "?", "{"]:
        return regexp

    # Sanity check
    if len(nodes) == 0:
        raise IncorrectRegexpException("No node before occurences node")
    
    if char == "*":
        min = 0
        max = None
        regexp = regexp[1:]
    elif char =="+":
        min = 1
        max = None
        regexp = regexp[1:]
    elif char == "?":
        min = 0
        max = 1
        regexp = regexp[1:]
    elif char == "{":
        # {n} or {n, m}
        values, regexp = regexp[1:].split("}", 1)
        str_min_max = values.split(",", 1)
        if len(str_min_max) == 1:
            min = int(str_min_max[0].strip())
            max = min
        else:
            min = int(str_min_max[0].strip())
            max = int(str_min_max[1].strip())

    last_node = nodes[-1]
    if isinstance(last_node, LiteralNode) and last_node.is_multichar():
        char = last_node.pop_last_char()
        nodes.append(OccurencesNode(min, max, LiteralNode(char)))
    else:
        nodes[-1] = OccurencesNode(min, max, nodes[-1])   

    return regexp
