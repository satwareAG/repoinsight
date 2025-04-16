#!/usr/bin/env python
"""
Detailed test script for the --gui flag.
This creates a test harness that intercepts several functions to track exactly what's happening.
"""

import sys
import logging
from unittest.mock import patch, MagicMock
import importlib

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create mock objects for tracking function calls
mock_run_app = MagicMock(return_value=0)
mock_run_app.__name__ = 'run_app'  # needed for some decorators

# List to capture command line args as they're processed
captured_args = []

def args_capturer(*args, **kwargs):
    """Capture arguments being passed to typer callback"""
    logger.debug(f"Callback called with: args={args}, kwargs={kwargs}")
    captured_args.append((args, kwargs))
    # Continue with original function
    return original_main(*args, **kwargs)

print("=" * 60)
print("Starting detailed GUI flag test")
print("=" * 60)

try:
    # Step 1: Patch gui.app.run_app to prevent actual GUI from launching
    with patch('repoinsight.gui.app.run_app', mock_run_app):
        # Get a reference to the CLI commands module
        from repoinsight.cli import commands
        
        # Step 2: Store reference to original main callback function
        original_main = commands.main
        
        # Step 3: Replace the main callback with our instrumented version
        commands.main = args_capturer
        
        # Test various command combinations
        test_cases = [
            ["--gui"],
            ["--gui", "--help"],
            ["run", "--help"],
            ["--version", "--gui"],
            ["--gui", "run", "--repository", "."]
        ]
        
        for i, args in enumerate(test_cases):
            print(f"\nTest case {i+1}: {' '.join(args)}")
            print("-" * 40)
            
            # Reset state for this test
            captured_args.clear()
            mock_run_app.reset_mock()
            
            # Import main module fresh to avoid state from previous tests
            if 'repoinsight.__main__' in sys.modules:
                del sys.modules['repoinsight.__main__']
            
            # Run the main function with our test arguments
            from repoinsight.__main__ import main
            try:
                exit_code = main(args)
                print(f"Exit code: {exit_code}")
            except SystemExit as e:
                print(f"SystemExit with code: {e.code}")
            except Exception as e:
                print(f"Exception: {type(e).__name__}: {e}")
            
            # Check if GUI was launched
            if mock_run_app.called:
                print("✓ GUI was launched")
                print(f"  Times called: {mock_run_app.call_count}")
            else:
                print("✗ GUI was NOT launched")
                
            # Print captured args if any
            if captured_args:
                print("Callback args captured:")
                for args_tuple in captured_args:
                    print(f"  - Args: {args_tuple[0]}, Kwargs: {args_tuple[1]}")
            
            print("-" * 40)
    
    print("\nFinal verification:")
    print("=" * 40)
    # Reset all our patches and mocks
    commands.main = original_main
    
    # Try direct test with our verification harness
    with patch('repoinsight.gui.app.run_app') as final_mock:
        final_mock.return_value = 0
        final_mock.__name__ = 'run_app'
        
        print("Running final test: 'python -m repoinsight --gui'")
        if 'repoinsight.__main__' in sys.modules:
            del sys.modules['repoinsight.__main__']
            
        from repoinsight.__main__ import main
        exit_code = main(["--gui"])
        
        if final_mock.called:
            print("TEST PASSED: --gui flag properly calls the GUI application")
        else:
            print("TEST FAILED: --gui flag did not launch the GUI application")
            
except Exception as e:
    import traceback
    print(f"Test framework error: {e}")
    traceback.print_exc()

print("\nDetailed test complete")
print("=" * 60)
