# %%
import tree_sitter_python as tspython
import tree_sitter_cpp as tscpp
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language(), "python")
CPP_LANGUAGE = Language(tscpp.language(), "cpp")

py_parser = Parser()
py_parser.set_language(PY_LANGUAGE)

cpp_parser = Parser()
cpp_parser.set_language(CPP_LANGUAGE)


def parse_code(parser: Parser, code: str):
    tree = parser.parse(bytes(code, "utf-8"))
    return tree


def main():
    with open("sample_code.py", "r") as f:
        py_code = f.read()

    tree = parse_code(py_parser, py_code)
    root = tree.root_node
    function_node = root.child_count
    # function_body_node = function_node.child_by_field_name("body")
    # if_stat_node = function_body_node.child(0)
    # cond = if_stat_node.child_by_field_name("condition")
    print(function_node)


if __name__ == '__main__':
    main()