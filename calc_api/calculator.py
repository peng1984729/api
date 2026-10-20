def op_sum(a: float, b: float) -> float:
    return a + b

def op_multiply(a: float, b: float) -> float:
    return a * b

def op_subtract(a: float, b: float) -> float:
    return a - b

def op_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("除数不能为 0!")
    return a / b

OPS = {
    "sum": op_sum,
    "multiply": op_multiply,
    "subtract": op_subtract,
    "divide": op_divide,
}

def calculate(operation: str, a: float, b: float) -> float:
    if operation not in OPS:
        raise ValueError(f"不支持的操作: {operation}")
    return OPS[operation](a, b)
