class NotFoundFileException(Exception):
    """Raised when the input file does not exist or is not found"""
    
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)