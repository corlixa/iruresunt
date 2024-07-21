def unwrap_function(nested_structure):
    """
    Recursively flattens a nested structure. If the input is a list of lists,
    it returns a single flattened list.
    
    Args:
        nested_structure (list): A nested list to flatten.
        
    Returns:
        list: A flattened version of the input nested list.
    """
    unwrapped = []
    for element in nested_structure:
        if isinstance(element, list):
            unwrapped.extend(unwrap_function(element))
        else:
            unwrapped.append(element)
    return unwrapped
