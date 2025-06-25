# Unused import

# Bad formatting
x = 1 + 2 * 3
y = x * 2 + 3 / 4

# Unused variables
unused_var = "I'm not used anywhere"
another_unused = 42

# Bad variable names
a = 1
b = 2
c = a + b


# Missing type hints
def bad_function(param1, param2):
    return param1 + param2


# Unused function
def unused_function():
    pass


# Bad string formatting
name = "John"
age = 25
print("Name: " + name + " Age: " + str(age))

# Long line that exceeds line length
very_long_line = "This is a very long line that should be broken up into multiple lines because it exceeds the maximum line length allowed by the code formatter and linter"

# Bad spacing around operators
result = 1 + 2 * 3 / 4 - 5


# Missing spaces after commas
def bad_commas(param1, param2, param3):
    return param1, param2, param3


# Extra blank lines


# And more extra blank lines


# Trailing whitespace here
def function_with_trailing_whitespace():
    return True


# Bad list formatting
bad_list = [1, 2, 3, 4, 5]

# Bad dict formatting
bad_dict = {"key1": "value1", "key2": "value2"}

# Unused exception variable
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error occurred")


# Bad class definition
class BadClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def badly_formatted_function(param1, param2, param3):
    """This is a badly formatted function with terrible spacing and formatting"""
    x = 1 + 2 * 3 / 4
    y = param1 + param2 * param3
    if x > y:
        print("x is greater")
    else:
        print("y is greater")
    return x, y


class BadlyFormattedClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.data = []

    def add_item(self, item):
        self.data.append(item)
        print(f"Added {item} to {self.name}")

    def get_items(self):
        return self.data


def another_bad_function():
    x = 10
    y = 20
    z = 30
    result = x + y + z
    print(f"Result: {result}")
    return result


# Badly formatted list and dict
bad_list = [1, 2, 3, 4, 5]
bad_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Terrible variable names and spacing
a = 1
b = 2
c = a + b
print(c)


# Inconsistent indentation
def bad_indentation():
    print("This has wrong indentation")
    print("This has different indentation")
    print("Back to wrong indentation")


print("test")
