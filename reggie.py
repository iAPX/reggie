
import app.exceptions as exceptions
from app.parse_regexp import parse_regexp
from app.nodes.startswith_node import StartsWithNode
from app.nodes.endswith_node import EndsWithNode
from app.helpers.helper_indent import indent_line


if __name__ == "__main__":
    # @see https://www.programiz.com/python-programming/regex
    # regex = "^ab"
    # regex = r"^abcdef$"
    # regex = r"^a...s$"
    # regex = r"[abc]"
    # regex = r"[a-e\d]"
    # regex = r"[0-39]"
    # regex = r"[^abc]"
    # regex = r"[+]"
    # regex = r"ma*n"
    # regex = r"ma+n"
    # regex = r"ma?n"
    # regex = r"xyza{2,3}toto"
    # regex = r"[0-9]{2,4}"
    # regex = r"[ \t\n\r\f\v]"
    # regex = r"^The.*Spain$"
    # regex = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
    regex = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"

    # regex = r"^(abc|def|ghi|jkl)zx$"       # Problem, maybe processed through the parse_regexp and recursivity?

    """
    regex = r"a|b|c"       # Problem, maybe processed through the parse_regexp and recursivity?
    regex = r"(a|b|c)xz"

    regex = r"\Athe"
    regex = r"\bfoo"
    regex = r"foo\b"
    regex = r"\Bfoo"
    regex = r"\d"
    regex = r"\D"
    regex = r"\s"
    regex = r"\S"
    regex = r"\w"
    regex = r"\W"
    regex = r"Python\Z"

    regex = r"[a-zA-Z0-9_]"
    regex = r"[^a-zA-Z0-9_]"


    regex = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
    regex = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
    """

    print("Regexp : ", regex)

    remaining_str, nodes = parse_regexp(regex)

    print("Remaining string:", remaining_str)
    print()

    print("Nodes:")
    for node in nodes:
        print(node)
    print()

    print("Reglll code:")
    if len(nodes) > 0 and not isinstance(nodes[0], StartsWithNode):
        print(indent_line("# !!!WARNING!!! The regexp doesn't start at the beginning of the string, see: StartsWith", 2))
    for node in nodes:
        print(node.generate_code(2), end="")
    if len(nodes) > 0 and not isinstance(nodes[-1], EndsWithNode):
        print(indent_line("# !!!WARNING!!! The regexp doesn't end at the ending of the string, see: EndsWith", 2))
    print()

    print("Regexp reconstitued code:")
    for node in nodes:
        print(node.generate_regexp(), end="")
    print()
    print(regex)
    print()
    
