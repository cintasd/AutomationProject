"""Convenience entry point for running the SMEC browser tests."""

import sys

import pytest


if __name__ == "__main__":
    raise SystemExit(pytest.main(["tests", *sys.argv[1:]]))
