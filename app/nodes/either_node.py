
from ..helpers.helper_indent import indent_line
from .base_node import BaseNode


class EitherNode(BaseNode):
    """
    Handles the either through stored alternatives on a list of Nodes
    """
    nodes: list[list[BaseNode]]

    def __init__(self, nodes: list[list[BaseNode]]):
        self.nodes = nodes

    # Returns the pseudo-language code corresponding to the node and its sub-nodes
    def generate_code(self, indent: int = 0) -> str:
        output = "\n"
        for sub_nodes in self.nodes:
            output += indent_line("Either", indent)
            for sub_node in sub_nodes:
                output += sub_node.generate_code(indent + 1)
        output += indent_line("EitherEnd", indent)
        output += "\n"

        return output
    
    # Returns the regexp corresponding to the node and its sub-nodes
    def generate_regexp(self) -> str:
        output = []
        for sub_nodes in self.nodes:
            sub_output = ""
            for sub_node in sub_nodes:
                sub_output += sub_node.generate_regexp()
            output.append(sub_output)

        return "|".join(output)
    
    def __str__(self) -> str:
        return f"Node: EitherNode ( {self.nodes} )"

