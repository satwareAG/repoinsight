#!/usr/bin/env python
"""
Simple verification script for the --gui flag.
This checks that the flag appears in the help output.
"""

import sys
import subprocess

def run_command(cmd):
    """Run a command and return its output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def main():
    print("Verifying --gui flag implementation")
    print("=" * 40)
    
    # Check if --gui appears in help output
    stdout, stderr, code = run_command([sys.executable, "-m", "repoinsight", "--help"])
    print(f"Return code: {code}")
    
    # Print the full help output for debugging
    print("\nHelp Output:")
    print("-" * 40)
    print(stdout)
    print("-" * 40)
    
    if "--gui" in stdout:
        print("SUCCESS: --gui flag is mentioned in help output")
        # Find the line containing --gui
        for line in stdout.split('\n'):
            if "--gui" in line:
                print(f"Found in help: {line}")
                break
    else:
        print("ERROR: --gui flag not found in help output")
    print("-" * 40)
    
    # Try invalid flag to verify error handling
    stdout, stderr, code = run_command([sys.executable, "-m", "repoinsight", "--invalid-flag"])
    print(f"Invalid flag test return code: {code}")
    if code != 0:
        print("SUCCESS: Invalid flag correctly causes error")
    else:
        print("ERROR: Invalid flag didn't cause error")
    print("-" * 40)
    
    print("Verification complete")

if __name__ == "__main__":
    main()
