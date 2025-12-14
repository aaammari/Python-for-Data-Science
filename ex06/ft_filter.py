def ft_filter(function_to_apply, iterable):
    """
        This function applies a filtering function to
        an iterable and returns a list of elements
        that satisfy the filtering condition.
    Args:
        function_to_apply: A function that returns True or False
        iterable: An iterable (like a list, tuple, etc.)
    Returns:
        A list of elements from the iterable that satisfy the condition
        defined by function_to_apply.
    """
    result = []
    for item in iterable:
        if function_to_apply(item):
            result.append(item)
    return result
