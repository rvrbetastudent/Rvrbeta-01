def list_to_string(names):
    """
    Converts a list of names into a comma-separated string with 'and' before the last name.
    """
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"

sibling_names = ['Ryan', 'Matt', 'Heidi']
print(f"Siblings: {list_to_string(sibling_names)}")