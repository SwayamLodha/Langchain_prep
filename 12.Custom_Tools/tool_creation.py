from langchain_core.tools import tool

# Step 1 -> Create a fucntion

def multiply(a, b):
    """Multiply two numbers"""
    return a*b

# Step 2 -> Add type hints

def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

# Step 3 -> Add tool decorator

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({"a":15, "b": 4})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)