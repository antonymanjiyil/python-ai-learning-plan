"""Auto-starter tests for Day 28 - Email Automation.
Replace these with real tests as you complete the day's challenge."""

import importlib

def test_imports():
    # Ensure the day's file imports without syntax errors
    mod = importlib.import_module('day28')
    assert hasattr(mod, 'main')
