# libraries imports
import matplotlib.pyplot as plt

# local files import
from classes.abstract.AbstractOperator import AbstractOperator

class IssuuOperator(AbstractOperator):
    """Holds the operator of an Issuu-syntaxed dataset"""


    def __init__(self, data):
        """Data has to be a pandas DataFrame. Do NOT instantiate without using the Factory method."""
        super().__init__(data)


    def _get_column(self, column):
        """Retrieves a value count from a given column of the dataset"""
        return self.data.as_dataframe()[column]

    def view_by_browser(self, simplified=False, plot=True):
        column = self._get_column("visitor_useragent")

        if (simplified):
            print(column)
            val_count = column.apply(lambda string: string.split("/")[0] if (type(string)==str) else None).value_counts()
            print(val_count)
        else:
            val_count = column.value_counts()

        if (plot):
            counts = val_count.values
            labels = [labl[0:17]+"..." for labl in val_count.index.values]
            
            # 'Qt4Agg' backend for fullscreen plot
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()

            plt.barh(range(len(val_count)), counts, align='center')
            plt.yticks(range(len(val_count)), labels, rotation="45", size='small')
            plt.ylabel("Names of browsers used (not simplified)")
            plt.xlabel("Value count of browsers usage")
            plt.title("Horizontal bar chart of the number of occurency of every browser")
            plt.show()
    
        