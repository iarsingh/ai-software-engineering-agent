from agentx.progression import se_agent

def test_se_agent_never_pushes():
    out = se_agent("open a PR for the failing test")
    assert out["pushed"] is False
    assert out["pr_opened"] is False

