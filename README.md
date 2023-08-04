# check_nocommit
check_nocommit is a pre-commit hook designed to check for '#NOCOMMIT' messages in text files.

It's a simple utility to leave yourself reminders not to check-in temporary edits into your repo that you would definitely be reminded of.

For pre-commit: see [https://github.com/pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)

## Configuration

```yaml
repos:
  - repo: https://github.com/akhilsbehl/check_nocommit
    rev: v0.1.0
    hooks:
      - id: check_nocommit
```

## Usage

### Inline reminders

```python
def this_function_that_is_being_debugged(*args):
    "docstring"
    var = "foo"
    print(var)  #NOCOMMIT
    do_something_with_var()
```

### Block reminders

```python
def this_function_that_is_being_debugged(*args):
    "docstring"
    var = "foo"
    #NOCOMMIT:START
    var += "bar for now"
    print(var)
    do_something_else_with_var()
    var = "foo"
    #NOCOMMIT:END
    do_something_with_var()
```

## License
This project is licensed under the terms of the MIT license. See the LICENSE file for the full license text.
