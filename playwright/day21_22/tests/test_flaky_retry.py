import pytest
import random

@pytest.mark.flaky
@pytest.mark.regression
def test_flaky_example():
    # Simulate flakiness: pass only 50% of the time
    value = random.choice([True, False])
    assert value, "Flaky failure: randomly chose False"
