def rotate_list(values: list, reversed: bool = False):
    """
    Rotate list, if not reveresed: [1, 2, 3] => [3, 1, 2]
    if reversed: [1, 2, 3] => [2, 3, 1]
    """
    if not reversed:
        last_val = values.pop(-1)
        values.insert(0, last_val)
    else:
        first_val = values.pop(0)
        values.append(first_val)

    return values
