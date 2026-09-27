import ast
import operator

# Supported operators
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.BitXor: operator.xor,
    ast.USub: operator.neg
}

def eval_expr(expr):
    """
    Safely evaluate a mathematical expression from a string.
    """
    def _eval(node):
        if isinstance(node, ast.Num): # <number>
            return node.n
        elif isinstance(node, ast.BinOp): # <left> <operator> <right>
            return operators[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
            return operators[type(node.op)](_eval(node.operand))
        else:
            raise TypeError(node)

    try:
        return _eval(ast.parse(expr, mode='eval').body)
    except Exception:
        return None

def calculate(expression: str) -> float:
    try:
        res = eval_expr(expression)
        return float(res) if res is not None else 0.0
    except Exception:
        return 0.0
