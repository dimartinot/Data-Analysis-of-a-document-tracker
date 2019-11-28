class UnknownInputException(Exception):
    """Raised when the command-line input takes an unknown value"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)