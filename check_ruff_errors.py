"""
Simple script to check if our configuration for B008 is working properly.
"""
import os
import sys
from pathlib import Path

# Use direct module imports for more reliable execution
try:
    from ruff.__main__ import find_ruff_bin

    ruff_path = find_ruff_bin()
except ImportError:
    print("Could not import ruff module. Make sure it's installed.")
    sys.exit(1)

# Path to the file to check
commands_path = Path("src/repoinsight/cli/commands.py").absolute()

if not commands_path.exists():
    print(f"File not found: {commands_path}")
    sys.exit(1)

print(f"Using ruff at: {ruff_path}")
print(f"Checking file: {commands_path}")
print(f"Current directory: {os.getcwd()}")
print("\nChecking for B008 errors...\n")

# Execute ruff directly
result = os.system(f"{ruff_path} check --select=B008 {commands_path}")

# Explain the result
if result == 0:
    print("\nSuccess! No B008 errors found. The configuration is working correctly.")
else:
    print("\nB008 errors still exist. The configuration may need adjustment.")

sys.exit(0 if result == 0 else 1)
