
from ..nodes.base_node import BaseNode

"""
Test-only parser
"""

def parse(regexp: str, nodes: list[BaseNode]) -> str:
    print("Test parser: " + regexp)
    return regexp
