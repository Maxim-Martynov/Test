import io
import sys
import os
import sys as py_sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from stringformat import print_formatted  # Adjust the import as necessary

def test_print_formatted(n, expected_output):
    # Capture the original stdout
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()  # Redirect stdout to capture prints


    print_formatted(n)

    # Get the printed output
    output = sys.stdout.getvalue()

    # Restore the original stdout
    sys.stdout = original_stdout

    # Expected output

    # Check if the output is as expected
    if output == expected_output:
        print("Test passed!")
    else:
        print("Test failed!")
        print("Expected:", repr(expected_output))
        print("Got:", repr(output))

# Run the test
test_print_formatted(1, ('1 1 1 1\n'))
test_print_formatted(0, 'Error\n')
test_print_formatted(100, 'Error\n')
