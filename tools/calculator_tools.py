from crewai.tools import BaseTool

class CalculatorTool(BaseTool):
    name: str = "Calculator Tool"
    description: str = "Useful to perform mathematical calculations like sum, minus, multiplication, division, etc."
    
    def _run(self, operation: str):
        """Perform the calculation with the given operation"""
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
