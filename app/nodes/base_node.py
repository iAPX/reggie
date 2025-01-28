
"""
Define a base node class.
Initializer will have a different signature for each Node type.

- generate_code() : Generate the code corresponding to the node and its sub-nodes
- generate_regexp() : Generate the regexp corresponding to the node and its sub-nodes
"""


class BaseNode:

    # Returns the pseudo-language code corresponding to the node and its sub-nodes
    def generate_code(self, indent: int = 0) -> str:
        raise NotImplementedError
    
    # Returns the regexp corresponding to the node and its sub-nodes
    def generate_regexp(self) -> str:
        raise NotImplementedError
