# local files import
from classes.abstract.AbstractOperator import AbstractOperator

class IssuuOperator(AbstractOperator):
    """Holds the operator of an Issuu-syntaxed dataset"""


    def __init__(self, data):
        """Data has to be a pandas DataFrame. Do NOT instantiate without using the Factory method."""
        super().__init__(self, data)


    def _view_by(self, column):
        pass

    def view_by_browser(self):
        pass
    
        