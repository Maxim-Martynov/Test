import io
import sys
import os
import sys as py_sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from firstlastname import print_full_name  # Adjust the import as necessary

def test_print_full_name():
    # Capture the original stdout
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()  # Redirect stdout to capture prints

    # Test case
    first_name = 'John'
    last_name = 'Doe'
    print_full_name(first_name, last_name)

    # Get the printed output
    output = sys.stdout.getvalue()

    # Restore the original stdout
    sys.stdout = original_stdout

    # Expected output
    expected_output = 'Hello John Doe! You just delved into python.\n'

    # Check if the output is as expected
    if output == expected_output:
        print("Test passed!")
    else:
        print("Test failed!")
        print("Expected:", repr(expected_output))
        print("Got:", repr(output))

# Run the test
test_print_full_name()
