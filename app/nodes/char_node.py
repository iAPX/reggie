
from ..helpers.helper_indent import indent_line
from ..helpers.helper_escape_char import escape_char
from .base_node import BaseNode


class CharNode(BaseNode):
    """
    Holds a single character within a sequence or others
    """

    char : str = ""

    def __init__(self, char: str):
        self.char = char

    # Returns the pseudo-language code corresponding to the node and its sub-nodes
    def generate_code(self, indent: int = 0) -> str:
        return indent_line("Char " + self.char, indent)
    
    # Returns the regexp corresponding to the node and its sub-nodes
    def generate_regexp(self) -> str:
        return escape_char(self.char)

    def __str__(self) -> str:
        return f"Node: CharNode ( {self.char} )"
