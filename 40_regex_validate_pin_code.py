def validate_pin(pin):
    """Regex validate PIN code

    Return:
        input pin code is exactly 4 digits or exactly 6 digits or not

    Args:
        pin code 
    
    Example:
        "1234" -> true
        "12345" -> false
    """
    return pin.isdigit() and len(pin) in [4, 6]