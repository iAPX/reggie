
import app.exceptions as exceptions
from app.parse_regexp import parse_regexp


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

    # regex = r"abc|def|ghi|jkl"       # Problem, maybe processed through the parse_regexp and recursivity?

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
    for node in nodes:
        print(node.generate_code(2), end="")
    print()

    print("Regexp reconstitued code:")
    for node in nodes:
        print(node.generate_regexp(), end="")
    print()
    print(regex)
    print()
    
