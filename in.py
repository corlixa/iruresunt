def find_duplicate_in_dict(d):
    seen = set()
    for key, value in d.items():
        if value in seen:
            return value  # Found duplicate, return the duplicate item
        seen.add(value)
    return None  # No duplicates found, return None
