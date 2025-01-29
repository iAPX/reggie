
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line


class OccurencesNode(BaseNode):
    min_occurences: int|None = 0
    max_occurences: int = 0
    node: BaseNode|None = None

    def __init__(self, min_occurences: int, max_occurences: int|None, node: BaseNode):
        self.min_occurences = min_occurences
        self.max_occurences = max_occurences
        self.node = node

    # Returns the pseudo-language code corresponding to the node and its sub-nodes
    def generate_code(self, indent: int = 0) -> str:
        max_output = ".." + str(self.max_occurences) if self.max_occurences is not None else "+"
        output = indent_line("Occurences " + str(self.min_occurences) + max_output, indent)
        output += self.node.generate_code(indent + 1)
        output += indent_line("EndOccurences", indent)
        output += "\n"
        return output
    
    # Returns the regexp corresponding to the node and its sub-nodes
    def generate_regexp(self) -> str:
        output = self.node.generate_regexp()
        if self.min_occurences == 0 and self.max_occurences == 1:
            return output + "?"
        elif self.min_occurences == 0 and self.max_occurences is None:
            return output + "*"
        elif self.min_occurences == 1 and self.max_occurences is None:
            return output + "+"
        elif self.min_occurences == self.max_occurences:
            return output + "{" + str(self.min_occurences) + "}"
        
        # Generic case
        return output + "{" + str(self.min_occurences) + "," + str(self.max_occurences) + "}"
    
    def __str__(self) -> str:
        return f"Node: OccurencesNode ( {self.min_occurences}, {self.max_occurences}, {self.node} )"
