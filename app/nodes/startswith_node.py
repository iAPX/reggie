
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line

class StartsWithNode(BaseNode):

    def generate_code(self, indent: int = 0) -> str:
        output = indent_line("# Starts at the beginning of the string", indent)
        output += indent_line("StartsWith", indent)
        output += "\n"
        return output
    
    def generate_regexp(self) -> str:
        return "^"

    def __str__(self) -> str:
        return "Node: StartsWith"
