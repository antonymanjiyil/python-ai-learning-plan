"""Auto-starter tests for Day 13 - JSON.
Replace these with real tests as you complete the day's challenge."""

import importlib

def test_imports():
    # Ensure the day's file imports without syntax errors
    mod = importlib.import_module('day13')
    assert hasattr(mod, 'main')
