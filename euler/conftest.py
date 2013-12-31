import pytest

slow = pytest.mark.slowtest


def pytest_addoption(parser):
    parser.addoption('--runslow', action='store_true', help='run slow tests')


def pytest_runtest_setup(item):
    if 'slow' in item.keywords and not item.config.getoption('--runslow'):
        pytest.skip('need --runslow option to run slow tests')