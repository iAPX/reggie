

from .base_node import BaseNode
from .set_node import SetNode
from ..helpers.helper_indent import indent_line

class SequenceNode(BaseNode):

    def generate_code(self, indent: int = 0) -> str:
        output = indent_line("StartsWith", indent) + "\n"
        output += "\n"
        return output
    
    def generate_regexp(self) -> str:
        return "^"
    
    def __str__(self) -> str:
        return f"Node: SequenceNode"

