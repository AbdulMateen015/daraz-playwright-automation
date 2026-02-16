import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Override browser context args to force maximization setup.
    """
    return {
        **browser_context_args,
        "no_viewport": True
    }

@pytest.fixture(scope="session")
def launch_args():
    """
    Launch arguments for the browser to start maximized.
    """
    return ["--start-maximized"]
