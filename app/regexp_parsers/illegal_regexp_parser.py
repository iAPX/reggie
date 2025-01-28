
from ..nodes.base_node import BaseNode
from ..exceptions import IllegalRegexpException



def parse(regexp: str, nodes: list[BaseNode]) -> str:
    # Avoid testing for empty regexp, or non-parsable regexp
    raise IllegalRegexpException(regexp)
