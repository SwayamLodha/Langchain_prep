from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")

def Multiply (a: int, b: int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func= Multiply,
    name="Multiply",
    description="Multiplication of two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"a":25, "b":4})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)