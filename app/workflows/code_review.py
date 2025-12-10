from app.engine.registry import get_tool

def extract_functions(state):
    """
    Extract basic metrics from the user's code.
    Counts functions and optionally uses tools (e.g., line counter).
    """
    code = state.get("code", "")

    # Count function definitions
    functions = code.count("def")
    state["functions"] = functions
    state["step"] = "extract_done"

    # Optional: Use pre-registered tool (e.g., count_lines)
    tool = get_tool("count_lines")
    if tool:
        state.update(tool(code))

    return state


def check_complexity(state):
    """
    Computes a simple rule-based complexity score.
    Complexity = number_of_functions * 2
    """
    complexity = state["functions"] * 2
    return {"complexity": complexity}


def detect_issues(state):
    """
    Counts potential issues based on missing function coverage.
    Issues = max(0, 5 - functions)
    """
    issues = max(0, 5 - state["functions"])
    return {"issues": issues}


def suggest_improvements(state):
    """
    Produces a quality score based on complexity and detected issues.
    Higher score = better code quality.
    """
    score = 10 - (state["complexity"] + state["issues"])
    return {"quality_score": score}


def should_loop(state):
    """
    Determines whether the workflow should loop.
    Loop continues until:
        quality_score >= threshold
    """
    return state["quality_score"] < state["threshold"]
