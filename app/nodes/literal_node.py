
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line

class LiteralNode(BaseNode):
    values: list[str] = []

    def __init__(self, chars: str):
        self.values = [chars]

    def add_char(self, chars: str):
        self.values.append(chars)
    
    def is_multichar(self) -> bool:
        return len(self.values) > 1

    def pop_last_char(self):
        chars = self.values[-1]
        self.values = self.values[:-1]
        return chars

    def generate_code(self, indent: int) -> str:
        values = [self.escape_code_value(value) for value in self.values]
        return indent_line("Literal " + " ".join(self.values), indent)
    
    def generate_regexp(self) -> str:
        values = [self.escape_regexp_value(value) for value in self.values]
        return "".join(self.values)

    def __str__(self) -> str:
        return f"Node: LiteralNode ( {self.values} )"

    def unescape_value(self, value: str) -> str:
        return value
    
    def escape_code_value(self, value: str) -> str:
        return value

    def escape_regexp_value(self, value: str) -> str:
        return value
