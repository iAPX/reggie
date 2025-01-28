

from ..nodes.base_node import BaseNode
from ..nodes.set_node import SetNode
from ..exceptions import IncorrectRegexpException


"""
Parse the Regexp string and return the list of nodes generated.

- "-" only at first
- char
- char1-char2
- \char
- ends with ]
"""

def parse(regexp: str, nodes : list[BaseNode]) -> str:
    # Is it the start of a sequence?
    if not regexp.startswith("["):
        return regexp
    regexp = regexp[1:]
    
    # Parse recursively the remaining
    # from ..parse_regexp import parse_regexp
    # regexp, nodes = parse_regexp(regexp[1:])

    chars = []
    except_chars = []
    invert = False

    # Special case, invert ^
    if regexp[0] == "^":
        invert = True
        regexp = regexp[1:]

    # Special case : - at the beginning, or after ^
    if regexp[0] == "-":
        # A lot of specific cases!
        chars.append("-")
        regexp = regexp[1:]

    while regexp[0] != "]":
        char = regexp[0]

        # special case, we except some characters
        if regexp[0] == "^":
            invert = True
            regexp = regexp[1:]
            continue

        elif char == "\\":
            new_entry = regexp[0:2]
            regexp = regexp[2:]
        elif regexp[1] == "-" and regexp[2] != "]":
            new_entry = regexp[0:3]
            regexp = regexp[3:]
        else:
            new_entry = char
            regexp = regexp[1:]

        if invert:
            except_chars.append(new_entry)
        else:
            chars.append(new_entry)

    print("Set Node : ", chars)
    nodes.append(SetNode(chars, except_chars))

    return regexp[1:]
