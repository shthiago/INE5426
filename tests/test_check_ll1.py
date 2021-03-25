import pytest

from utils.check_ll1 import CfgProccessor


@pytest.fixture
def example_file() -> str:
    return 'tests/example.csf'


@pytest.fixture
def correct_firsts() -> dict:
    return {
        'S': {'a', 'b', 'c', 'd'},
        'A': {'a', '&'},
        'B': {'a', 'b', 'd', '&'},
        'a': {'a'},
        'b': {'b'},
        'c': {'c'},
        'd': {'d'}
    }


@pytest.fixture
def correct_follows() -> dict:
    return {
        'S': {'$'},
        'A': {'a', 'b', 'c', 'd'},
        'B': {'c'}
    }


def test_proc_first(example_file: str, correct_firsts: dict) -> str:
    cfg_proc = CfgProccessor()
    cfg_proc.read(example_file)

    for key, value in correct_firsts.items():
        print('Checking for non-terminal', key)
        assert cfg_proc.first(key) == value  # nosec


def test_proc_follow(example_file: str, correct_follows: dict) -> str:
    cfg_proc = CfgProccessor()
    cfg_proc.read(example_file)

    for key, value in correct_follows.items():
        print('Checking for non-terminal', key)
        assert cfg_proc.follow(key) == value  # nosec
