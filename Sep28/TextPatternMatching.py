def custom_strip(s: str, chars: str = None) -> str:
    """
    Works like Python's strip() method.
    
    - If chars is None, remove whitespace from both ends of the string.
    - Otherwise, remove all leading and trailing characters found in chars.
    """

    if chars is None:
        # Default behavior: strip whitespace
        chars = " \t\n\r\f\v"

    start = 0
    end = len(s) - 1

    # Trim from the left
    while start <= end and s[start] in chars:
        start += 1

    # Trim from the right
    while end >= start and s[end] in chars:
        end -= 1

    return s[start:end+1]


# Examples:
print(custom_strip("   hello   "))            # "hello"
print(custom_strip("xxhelloxx", "x"))         # "hello"
print(custom_strip("..!!test!!..", ".!"))     # "test"
# The output of the above examples should always exclude quotes, dead spaces, newlines, tabs, etc. the 
# only time you should see newtab is appropriately in each string entry.