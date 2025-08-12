
# 30-Day Python + AI Learning Plan (VS Code, Windows)

**Created:** 2025-08-12 12:42 UTC

## Getting Started
1. Open this folder in VS Code.
2. Create & activate a virtual environment (Windows PowerShell):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run a day's file:
   ```powershell
   python day01.py
   ```
5. Run tests:
   ```powershell
   pytest
   ```

## Tips
- Use an AI assistant (Copilot/Codeium/Continue) inside VS Code.
- Ask it to refactor, explain, or generate tests, but try coding first yourself.
- Keep all code changes inside the corresponding `dayXX.py` and `tests/test_dayXX.py`.

## Structure
- `day01.py` ... `day30.py` — one file per day with the challenge and AI prompts in the docstring.
- `tests/` — starter tests that at least import each file.
- `requirements.txt` — minimal dependencies (`pytest`, `requests` for API days).

Have fun and ship something small every day!
