
from .base_node import BaseNode
from ..helpers.helper_escape_char import escape_char
from ..helpers.helper_indent import indent_line


class SetNode(BaseNode):
    chars : list[str] = []
    except_chars: list[str] = []

    def __init__(self, chars: list[str], except_chars: list[str]):
        self.chars = chars
        self.except_chars = except_chars

    def generate_code(self, indent: int = 0) -> str:
        output = " ".join(self.grouped_chars(self.chars))
        if len(self.except_chars) > 0:
            output += " Except " + " ".join(self.grouped_chars(self.except_chars))
        return indent_line("Set " + output, indent)
    
    def generate_regexp(self) -> str:
        output = "".join(self.grouped_chars(self.chars))
        if len(self.except_chars) > 0:
            output += "^" + "".join(self.grouped_chars(self.except_chars))
        return "[" + output + "]"

    # @TODO escape chars
    # @TODO Group chars, for example \d for 0-9, and so on
    def grouped_chars(self, chars) -> list[str]:
        return chars

    def __str__(self) -> str:
        return f"Node: SetNode ( {self.chars},  {self.except_chars} )"
