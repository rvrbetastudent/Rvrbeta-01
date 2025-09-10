def list_to_string(lst):
    
    if not lst:
        return ""
    
    result = ", ".join(lst[:-1])
    if len(lst) > 1:
        result += ", and " + lst[-1]
    else:
        result += lst[-1]
    
    return result
print (list_to_string(['Ryan', 'Matt', 'Heidi'])) ## Prints out sibling names in a comma format.
    