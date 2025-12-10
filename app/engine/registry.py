
def count_lines(code: str):
    return {"lines": len(code.split("\n"))}

registry = {
    "count_lines": count_lines
}

def get_tool(name: str):
    """Retrieve a registered tool by name."""
    return registry.get(name)

def register_tool(name: str, func):
    """Register a new tool dynamically."""
    registry[name] = func
