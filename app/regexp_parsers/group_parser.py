
from ..nodes.base_node import BaseNode
from ..nodes.group_node import GroupNode
from ..exceptions import IncorrectRegexpException


def parse(regexp: str, nodes: list[BaseNode]) -> str:
    # Is it the start of a group?
    if not regexp.startswith("("):
        return regexp

    print("Group node")

    capturing_group = True
    if regexp[:3] == "(?:":
        print("Non Capturing group")
        capturing_group = False
        regexp = regexp[3:]
    else:
        regexp = regexp[1:]

    # Parse recursively the remaining
    from ..parse_regexp import parse_regexp
    regexp, sub_nodes = parse_regexp(regexp)

    # Check for the end of the sequence
    if not regexp.startswith(")"):
        raise IncorrectRegexpException("Unexpected end of Group: " + regexp)
    
    # Adds the subnodes into a GroupNode, and add it to the list
    nodes.append(GroupNode(sub_nodes, capturing_group))

    return regexp[1:]
