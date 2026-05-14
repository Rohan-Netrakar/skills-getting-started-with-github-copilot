import copy

import pytest

from src.app import activities

original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    from src.app import app

    return TestClient(app)
