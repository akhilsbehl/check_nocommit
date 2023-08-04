import unittest
import os
from checker import check_for_nocommit

class TestNoCommitChecker(unittest.TestCase):

    def test_check_for_nocommit(self):
        with open('temp.py', 'w') as f:
            f.write("#NOCOMMIT\n")
            f.write("print('Hello, World!')\n")
            f.write("#NOCOMMIT: START\n")
            f.write("print('This is a test.')\n")
            f.write("#NOCOMMIT: END\n")
            f.write("print('Goodbye, World!')\n")

        expected_output = [
            (1, "#NOCOMMIT"),
            (3, "#NOCOMMIT: START"),
            (4, "print('This is a test.')"),
            (5, "#NOCOMMIT: END"),
        ]

        self.assertEqual(check_for_nocommit('temp.py'), expected_output)

        os.remove('temp.py')

def test_check_for_nocommit_bash(self):
    with open('temp.sh', 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("#NOCOMMIT\n")
        f.write("echo 'Hello, World!'\n")
        f.write("#NOCOMMIT: START\n")
        f.write("echo 'This is a test.'\n")
        f.write("#NOCOMMIT: END\n")
        f.write("echo 'Goodbye, World!'\n")

    expected_output = [
        (2, "#NOCOMMIT"),
        (4, "#NOCOMMIT: START"),
        (5, "echo 'This is a test.'"),
        (6, "#NOCOMMIT: END"),
    ]

    self.assertEqual(check_for_nocommit('temp.sh'), expected_output)

    os.remove('temp.sh')

if __name__ == '__main__':
    unittest.main()
