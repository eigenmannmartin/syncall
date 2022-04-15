import logging
from pathlib import Path

import pytest
from _pytest.logging import caplog as _caplog  # type: ignore
from bubop import PrefsManager
from loguru import logger

from .conftest_gkeep import *
from .conftest_notion import *
from .conftest_tw import *


@pytest.fixture()
def test_data() -> Path:
    return Path(__file__).absolute().parent / "test_data"


@pytest.fixture
def caplog(_caplog):
    """
    Fixture that forwards loguru's output to std logging's output so that you can use caplog
    as usual
    """

    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    logger.add(PropogateHandler(), format="{message}")
    yield _caplog


class MockPrefsManager(PrefsManager):
    def __init__(self):
        self._conts = {
            "kalimera": {"a": 1, "b": 2, "c": [1, 2, 3]},
            "kalispera": {"a": 1},
            "kalinuxta": {"a": 2},
        }

        self._config_file = Path("TBD")

    def _cleanup(self):
        pass


@pytest.fixture()
def mock_prefs_manager() -> MockPrefsManager:
    return MockPrefsManager()
