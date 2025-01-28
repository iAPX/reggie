

from .base_node import BaseNode
from ..helpers.helper_indent import indent_line


class EndsWithNode(BaseNode):

    def generate_code(self, indent: int = 0) -> str:
        output = "\n"
        output += indent_line("# Ends at the end of the string", indent)
        output += indent_line("EndsWith", indent)
        return output
    
    def generate_regexp(self) -> str:
        return "$"

    def __str__(self) -> str:
        return f"Node: EndsWith"
