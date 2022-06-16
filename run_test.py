#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import pytest

# https://discuss.python.org/t/testing-doctests-breaks-src-layout/3728
# https://coverage.readthedocs.io/en/coverage-5.2.1/cmd.html


# pytest tests/test_module_seqrecord.py --cov=pydna --cov-append
# --cov-report=html --cov-report=xml --capture=no --durations=10
# --import-mode=importlib --nbval --current-env --doctest-modules
# --capture=no -vvv


def main():
    """docstring."""
    arg = sys.argv[-1] if len(sys.argv) > 1 else ""

    args = [
        f"src/{arg}",  # doctestdir
        "--cov=CAI",
        "--cov-append",
        "--cov-report=html",
        "--cov-report=xml",
        "--capture=no",
        "--durations=10",
        "--import-mode=importlib",
        "--nbval",
        "--current-env",
        "--doctest-modules",
        "--capture=no",
        "-vvv",
    ]

    result_suite_src = pytest.main(args)

    args = [
        f"tests/{arg}",  # test suite
        "--cov=CAI",
        "--cov-append",
        "--cov-report=html",
        "--cov-report=xml",
        "--capture=no",
        "--durations=10",
        "--import-mode=importlib",
        "--nbval",
        "--current-env",
        "--doctest-modules",
        "--capture=no",
        "-vvv",
    ]

    result_suite_tests = pytest.main(args)

    return result_suite_tests and result_suite_src


if __name__ == "__main__":
    result = main()
    sys.exit(int(result))