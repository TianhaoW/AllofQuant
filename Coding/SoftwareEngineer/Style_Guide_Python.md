# PEP 8 – Style Guide for Python Code
## Import
- Place imports at the top of the file.
- Use separate lines for each import.
- Group imports in this order, with blank lines between groups:
  1. Standard library imports.
  2. Third-party imports.
  3. Local application imports.

- Avoid wildcard imports (e.g., `from module import *`)

## Naming Conventions
### Variable Names

- **Style**: use `snake_case` (lowercase letters with underscores separating words).
- **Example**:
```python
max_value = 100
user_name = "your name"
```
- **Best Practices**:
  - Use `_` as a prefix for private/internal variables.

### Function Names:

- **Style**: use `snake_case`
- **Example**:
```python
def calculate_sum(a, b):
    return a + b
```
- **Best Practices**:
  - Use verbs or verb phrases to indicate the action of the function.
  - Prefix private/internal functions with an underscore (e.g., `_helper_function`).

### Class Names:

- **Style**: Use `CamelCase`
- **Example**:
```python
class DataProcessor:
    pass

class MyCustomException(Exception):
    pass
```
- **Best Practices**:
  - Use nouns or noun phrases that describe the purpose of the class.

### Constants

- **Style**: Use `ALL_CAPS` with underscores to separate words.
- **Example**:
```python
MAX_CONNECTIONS = 10
PI = 3.14159
```

### Modules and Package Names

- **Style**: 
  - For module (file) names: Use snake_case or short lowercase names.
  - For package names (directories): Use all lowercase, preferably without underscores.
- **Example**:
```plaintext
file_util.py
util/
```

## Functions and Method Arguments
### Default Argument Values
- Never use mutable objects (e.g., lists or dictionaries) as default values
```python
# Wrong example
def append(element, target = []):
    target.append(element)
    return target
```
The issue that the default value is evaluated only once, when the function is defined, and not each time the function is called. This can lead to unexpected behavior
```python
first_list = append(5)   # first_list will be [5]
second_list = append(10) # Both first_list and second_list will be [5, 10]
```
Here is the correct way to write this function
```python
def append(element, target = None):
    if target is None:
        target = []
    target.append(element)
    return target
```