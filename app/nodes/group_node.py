
from .base_node import BaseNode
from ..helpers.helper_indent import indent_line


class GroupNode(BaseNode):
    nodes: list[BaseNode]
    capturing_group: bool

    def __init__(self, nodes: list[BaseNode], capturing_group: bool):
        self.nodes = nodes
        self.capturing_group = capturing_group

    def generate_code(self, indent: int) -> str:
        option = "Capturing" if self.capturing_group else "NonCapturing"
        output = indent_line("Group " + option, indent)
        for node in self.nodes:
            output += node.generate_code(indent + 1)

        # For cleanliness we add an empty line
        # output += "\n"

        return output
    
    def generate_regexp(self) -> str:
        regexp = "("
        if not self.capturing_group:
            regexp += "?:"  

        for node in self.nodes:
            regexp += node.generate_regexp()
        regexp += ")"

        return regexp

    def __str__(self) -> str:
        return f"Node: GroupNode ( {self.nodes} )"
