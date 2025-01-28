
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line

class LiteralNode(BaseNode):
    value: list[str] = []

    def __init__(self, chars: str):
        self.value = [chars]

    def add_char(self, chars: str):
        self.value.append(chars)
    
    def is_multichar(self) -> bool:
        return len(self.value) > 1

    def pop_last_char(self):
        chars = self.value[-1]
        self.value = self.value[:-1]
        return chars

    def generate_code(self, indent: int) -> str:
        return indent_line("Literal " + " ".join(self.value), indent)
    
    def generate_regexp(self) -> str:
        return "".join(self.value)

    def __str__(self) -> str:
        return f"Node: LiteralNode ( {self.value} )"
