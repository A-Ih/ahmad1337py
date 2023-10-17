from typing import Literal
import pytest
from hamcrest import assert_that, equal_to, calling
from hamcrest.core.core.raises import raises
from typeguard import typechecked
from contextlib import nullcontext as no_raise
import json
import tempfile
from pathlib import Path

import lib.utils as utils
import lib.settings as settings

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 2, 5),
    (3, 4, 7),
    (2, 3, 5),
])
@typechecked
def test_two_sum(a: int, b: int, expected: int):
    assert_that(utils.two_sum(a, b), equal_to(expected))
    assert_that(utils.two_sum(b, a), equal_to(expected))

@pytest.mark.parametrize("condition, msg, should_raise", [
    (True, "Indeed there is no exception!", False),
    (False, "There is an exception!", True),
])
@typechecked
def test_require(condition: bool, msg: str, should_raise: bool):
    assert_that(
        calling(utils.require).with_args(condition, lambda: msg), 
        raises(utils.RequirementError, pattern=msg) if should_raise else no_raise()
    )
    

def test_get_settings():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "settings.json"
        with open(path, "w") as f:
            f.write(json.dumps({"n_jobs": 13, "seed": 42}))
        assert_that(settings.get_settings(path), equal_to(settings.Settings(n_jobs=13, seed=42)))
