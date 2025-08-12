"""Auto-starter tests for Day 24 - Inheritance.
Replace these with real tests as you complete the day's challenge."""

import importlib

def test_imports():
    # Ensure the day's file imports without syntax errors
    mod = importlib.import_module('day24')
    assert hasattr(mod, 'main')
