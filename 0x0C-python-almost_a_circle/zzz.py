def validate_integer(self, name, value):
    """Validation for integers and values"""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if name in ["x", "y"] and value < 0:
        raise ValueError(f"{name} must be >= 0")
    elif name in ["width", "height", "size"] and value <= 0:
        raise ValueError(f"{name} must be > 0")


def validate_integer(self, name, value):
    """Validation for integers and values"""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if name in ["x", "y"] and value < 0:
        raise ValueError(f"{name} must be >= 0")
    elif name in ["width", "height"] and value <= 0:
        raise ValueError(f"{name} must be > 0")
