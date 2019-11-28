class IncorrectInputDataException(Exception):
    """Raised when the input data has an incorrect format"""
    
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)