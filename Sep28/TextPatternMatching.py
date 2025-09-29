from typing import Optional

_WHITESPACE_CHARS = " \t\n\r\f\v"


def custom_strip(text: str, chars: Optional[str] = None) -> str:
    """
    Remove leading and trailing characters similarly to `str.strip()`.

    - If `chars` is None, remove ASCII whitespace from both ends.
    - Otherwise, remove any leading/trailing characters found in `chars`.

    Examples:
    >>> custom_strip("   hello   ")
    'hello'
    >>> custom_strip("xxhelloxx", "x")
    'hello'
    >>> custom_strip("..!!test!!..", ".!")
    'test'
    """
    if not text:
        return text

    remove_chars = _WHITESPACE_CHARS if chars is None else chars
    remove_set = set(remove_chars)  # O(1) membership checks for long `chars`

    start_idx = 0
    end_idx = len(text) - 1

    while start_idx <= end_idx and text[start_idx] in remove_set:
        start_idx += 1

    while end_idx >= start_idx and text[end_idx] in remove_set:
        end_idx -= 1

    return text[start_idx : end_idx + 1]


if __name__ == "__main__":
    print(custom_strip("   hello   "))
    print(custom_strip("xxhelloxx", "x"))
    print(custom_strip("..!!test!!..", ".!"))