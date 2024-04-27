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
    with open("samples/sample_code.py", "r") as f:
        py_code = f.read()

    tree = parse_code(py_parser, py_code)
    root = tree.root_node
    for chiled in root.children:
        function_body_node = chiled.child_by_field_name("body")
        for child in function_body_node.children:
            cond = child.child_by_field_name("condition")
            if cond is not None:
                print(f"cond: {py_code[cond.start_byte:cond.end_byte]}")
                print(f"{cond.sexp()=}")
                
            consq = child.child_by_field_name("consequence")
            if consq is not None:
                print(f"consq: {py_code[consq.start_byte:consq.end_byte]}")
            alter = child.child_by_field_name("alternative")
            if alter is not None:
                print(f"alter: {py_code[alter.start_byte:alter.end_byte]}")
            

    #         # print(cpp_code[cond.start_byte:cond.end_byte])
    #         # print(f"{if_stat_node=}")
    #         # print(if_stat_node.sexp())
    #         print(f"{child.sexp()}")


if __name__ == "__main__":
    main()
# %%
