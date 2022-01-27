# File to test different function of the project

import pytest
from src.test_file import function_pull_request
import logging


def test_1():

    logging.info("Running test_1")

    a = 1
    b = 3
    expected_result = 4
    assert function_pull_request(a, b) == expected_result

    return 0


def test_2():

    logging.info("Running test_2")

    a = 8
    b = 4
    expected_result = 12
    assert function_pull_request(a, b) == expected_result

    return 0
