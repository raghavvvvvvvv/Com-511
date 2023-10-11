def main():
    # Type checking
    num = 42
    string = "Hello, World!"
    lst = [1, 2, 3]
    dct = {"key": "value"}
    boolean = True

    print("Type Checking:")
    check_and_print("num", num, int)
    check_and_print("string", string, str)
    check_and_print("lst", lst, list)
    check_and_print("dct", dct, dict)
    check_and_print("boolean", boolean, bool)

    # Using built-in functions
    print("\nUsing Built-in Functions:")
    print("\n")
    # abs() - Returns the absolute value of a number
    num = -5
    result = abs(num)
    print(f"Absolute value of {num}: {result}")
    print("\n")

    # len() - Returns the length of an object (e.g., string, list)
    string = "Python"
    result = len(string)
    print(f"Length of '{string}': {result}")
    print("\n")

    # min() - Returns the minimum element from an iterable
    numbers = [5, 2, 8, 1, 7]
    result = min(numbers)
    print(f"Minimum value in {numbers}: {result}")
    print("\n")

    # round() - Rounds a floating-point number to a specified number of decimal places
    pi = 3.14159
    result = round(pi, 2)
    print(f"Rounded value of pi: {result}")
    print("\n")

    # isalnum() - Checks if a string consists of alphanumeric characters
    alnum_str = "Python123"
    result = alnum_str.isalnum()
    print(f"'{alnum_str}' is alphanumeric? {result}")
    print("\n")

    # type() - Returns the type of an object
    var = 42
    result = type(var).__name__
    print(f"Type of 'var': {result}")
    print("\n")

def check_and_print(name, value, data_type):
    result = isinstance(value, data_type)
    print(f"Is '{name}' of type {data_type.__name__}? {result}")

if __name__ == "__main__":
    main()
