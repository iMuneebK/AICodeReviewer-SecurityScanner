import ast

def analyze_code_ast(code_str):
    try:
        tree = ast.parse(code_str)
        func_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
        return {"syntax_valid": True, "functions_found": func_count}
    except Exception as e:
        return {"syntax_valid": False, "error": str(e)}
