
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line


class AnyCharNode(BaseNode):

    # Returns the pseudo-language code corresponding to the node and its sub-nodes
    def generate_code(self, indent: int = 0) -> str:
        return indent_line("AnyChar", indent)
    
    # Returns the regexp corresponding to the node and its sub-nodes
    def generate_regexp(self) -> str:
        return "."

    def __str__(self) -> str:
        return "Node: AnyChar"
