TOOLS = ["plan", "draft_patch", "run_tests"]
WRITES = ("git push", "merge", "force push",)

def run(goal, payload):
    if not goal or not str(goal).strip():
        raise ValueError("goal is empty")
    low = goal.lower()
    if any(w in low for w in WRITES):
        return {"refused": True, "reason": "destructive action requires a human", "applied": False, "tools": []}
    result = ["add test", "change handler"]
    return {"refused": False, "tools": TOOLS, "plan": result, "applied": False, "needs_approval": False}
