def page(items, number, size):
    """Return a one-based page of items."""
    if number < 1 or size < 1:
        raise ValueError('number and size must be positive')
    start = number * size
    return items[start:start + size]
