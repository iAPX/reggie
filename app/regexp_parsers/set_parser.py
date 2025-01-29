

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

    def get_next_char(regexp: str) -> tuple[str, str]:
        chars = regexp[0]
        if chars == "\\":
            chars = regexp[:2]
            regexp = regexp[2:]
            if chars == "\\x":
                chars += regexp[:2]
                regexp = regexp[2:]
        else:
            regexp = regexp[1:]
        return chars, regexp


    # Is it the start of a sequence?
    if not regexp.startswith("["):
        return regexp
    regexp = regexp[1:]
    
    chars = []
    except_chars = []
    invert = False

    while regexp[0] != "]":
        # special case, we except some characters
        if regexp[0] == "^":
            invert = True
            regexp = regexp[1:]
            continue

        new_entry, regexp = get_next_char(regexp)
        # Notice that "-" (dash) is only processed as rangge if immediately following a character, not a range or ^
        if regexp[0] == "-" and regexp[1] != "]":
            new_entry_range, regexp = get_next_char(regexp[1:])
            new_entry += "-" + new_entry_range

        if invert:
            except_chars.append(new_entry)
        else:
            chars.append(new_entry)

    print("Set Node : ", chars)
    nodes.append(SetNode(chars, except_chars))

    return regexp[1:]
