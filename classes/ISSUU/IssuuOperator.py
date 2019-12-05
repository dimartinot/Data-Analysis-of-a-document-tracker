# libraries imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from graphviz import Digraph
import os
import platform

# local files import
from classes.abstract.AbstractOperator import AbstractOperator
from classes.exception.IncorrectInputDataException import IncorrectInputDataException

class IssuuOperator(AbstractOperator):
    """Holds the operator of an Issuu-syntaxed dataset"""

    _GRAPHVIZ_W_BIN_PATH = "bin/windows/graphviz/release/bin"

    COUNTRY_TO_CONTINENT_MAPPING = {"AD":"EU","AE":"AS","AF":"AS","AG":"NA","AI":"NA","AL":"EU","AM":"AS","AN":"NA","AO":"AF","AP":"AS","AQ":"AN","AR":"SA","AS":"OC","AT":"EU","AU":"OC","AW":"NA","AX":"EU","AZ":"AS","BA":"EU","BB":"NA","BD":"AS","BE":"EU","BF":"AF","BG":"EU","BH":"AS","BI":"AF","BJ":"AF","BL":"NA","BM":"NA","BN":"AS","BO":"SA","BR":"SA","BS":"NA","BT":"AS","BV":"AN","BW":"AF","BY":"EU","BZ":"NA","CA":"NA","CC":"AS","CD":"AF","CF":"AF","CG":"AF","CH":"EU","CI":"AF","CK":"OC","CL":"SA","CM":"AF","CN":"AS","CO":"SA","CR":"NA","CU":"NA","CV":"AF","CX":"AS","CY":"AS","CZ":"EU","DE":"EU","DJ":"AF","DK":"EU","DM":"NA","DO":"NA","DZ":"AF","EC":"SA","EE":"EU","EG":"AF","EH":"AF","ER":"AF","ES":"EU","ET":"AF","EU":"EU","FI":"EU","FJ":"OC","FK":"SA","FM":"OC","FO":"EU","FR":"EU","FX":"EU","GA":"AF","GB":"EU","GD":"NA","GE":"AS","GF":"SA","GG":"EU","GH":"AF","GI":"EU","GL":"NA","GM":"AF","GN":"AF","GP":"NA","GQ":"AF","GR":"EU","GS":"AN","GT":"NA","GU":"OC","GW":"AF","GY":"SA","HK":"AS","HM":"AN","HN":"NA","HR":"EU","HT":"NA","HU":"EU","ID":"AS","IE":"EU","IL":"AS","IM":"EU","IN":"AS","IO":"AS","IQ":"AS","IR":"AS","IS":"EU","IT":"EU","JE":"EU","JM":"NA","JO":"AS","JP":"AS","KE":"AF","KG":"AS","KH":"AS","KI":"OC","KM":"AF","KN":"NA","KP":"AS","KR":"AS","KW":"AS","KY":"NA","KZ":"AS","LA":"AS","LB":"AS","LC":"NA","LI":"EU","LK":"AS","LR":"AF","LS":"AF","LT":"EU","LU":"EU","LV":"EU","LY":"AF","MA":"AF","MC":"EU","MD":"EU","ME":"EU","MF":"NA","MG":"AF","MH":"OC","MK":"EU","ML":"AF","MM":"AS","MN":"AS","MO":"AS","MP":"OC","MQ":"NA","MR":"AF","MS":"NA","MT":"EU","MU":"AF","MV":"AS","MW":"AF","MX":"NA","MY":"AS","MZ":"AF","NA":"AF","NC":"OC","NE":"AF","NF":"OC","NG":"AF","NI":"NA","NL":"EU","NO":"EU","NP":"AS","NR":"OC","NU":"OC","NZ":"OC","O1":"--","OM":"AS","PA":"NA","PE":"SA","PF":"OC","PG":"OC","PH":"AS","PK":"AS","PL":"EU","PM":"NA","PN":"OC","PR":"NA","PS":"AS","PT":"EU","PW":"OC","PY":"SA","QA":"AS","RE":"AF","RO":"EU","RS":"EU","RU":"EU","RW":"AF","SA":"AS","SB":"OC","SC":"AF","SD":"AF","SE":"EU","SG":"AS","SH":"AF","SI":"EU","SJ":"EU","SK":"EU","SL":"AF","SM":"EU","SN":"AF","SO":"AF","SR":"SA","ST":"AF","SV":"NA","SY":"AS","SZ":"AF","TC":"NA","TD":"AF","TF":"AN","TG":"AF","TH":"AS","TJ":"AS","TK":"OC","TL":"AS","TM":"AS","TN":"AF","TO":"OC","TR":"EU","TT":"NA","TV":"OC","TW":"AS","TZ":"AF","UA":"EU","UG":"AF","UM":"OC","US":"NA","UY":"SA","UZ":"AS","VA":"EU","VC":"NA","VE":"SA","VG":"NA","VI":"NA","VN":"AS","VU":"OC","WF":"OC","WS":"OC","YE":"AS","YT":"AF","ZA":"AF","ZM":"AF","ZW":"AF"}

    def __init__(self, data):
        """Data has to be a pandas DataFrame. Do NOT instantiate without using the Factory method."""
        super().__init__(data)

    def doc_id_exists(self, doc_id):
        """Returns true if doc id is found in the dataset"""
        df = self._get_dataframe()
        col = df[(df['subject_type'] == 'doc') & (df['subject_doc_id'] == doc_id)]['visitor_country']
        return (col.empty == False)

    def user_id_exists(self, user_id):
        """Returns true if user id is found in the dataset"""
        df = self._get_dataframe()
        col = df[df['visitor_uuid'] == user_id]['visitor_country']
        return (col.empty == False)

    def _get_dataframe(self):
        """Retrieves a value count from a given column of the dataset"""
        return self.data.as_dataframe()

    def _plot_frequency_table(self, val_count, x_label="Counts", y_label="Values", title="Frequency bar chart"):
        """Plots a frequency table"""
        counts = val_count.values
        labels = [labl[0:17]+"..." for labl in val_count.index.values]
        
        _, ax = plt.subplots()

        # 'Qt4Agg' backend for fullscreen plot
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

        for i, v in enumerate(counts):
            ax.text(v, i, " "+str(v), color='blue', va='center', fontweight='bold')

        ax.barh(range(len(val_count)), counts, align='center')
        
        plt.yticks(range(len(val_count)), labels, rotation="45", size='small')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)

        plt.show()
    
    def _readers_of(self, doc_id):
        """Get all the readers of the given document"""

        df = self._get_dataframe()

        df_readers_of = (df[(df['subject_type'] == 'doc') & (df['event_type'] == 'pageread') & (df['subject_doc_id'] == doc_id)])[['visitor_uuid']]
        df_readers_of = df_readers_of.drop_duplicates()

        return df_readers_of
    
    def _has_read(self, visitor_id):
        """Gets all the docs read by the given user"""
        df = self._get_dataframe()
        
        df_has_read = (df[(df['subject_type'] == 'doc') & (df['event_type'] == 'pageread') & (df['visitor_uuid'] == visitor_id)])[['subject_doc_id']]
        df_has_read = df_has_read.drop_duplicates()

        return df_has_read
    
    def get_dataset_path(self):
        return self.data.get_path()

    def view_by_browser(self, simplified=False, plot=True):
        """Implements the view by browser functionality"""
        column = self._get_dataframe()["visitor_useragent"]

        if (simplified):
            val_count = column.apply(lambda string: string.split("/")[0] if (type(string)==str) else None).value_counts()
        else:
            # we keep the 20 best
            val_count = column.value_counts()[:20]

        if (plot):
            self._plot_frequency_table(
                val_count, 
                y_label="Names of browsers used (not simplified)", 
                x_label="Value count of browsers usage",
                title="Horizontal bar chart of the number of occurency of every browser"
            )
        
        return val_count
    
    def view_by_country(self, doc_id, plot=True):
        """Implements the view by country functionality"""
        if (doc_id is None):
            raise IncorrectInputDataException()

        tmp_df = self._get_dataframe()
        
        column = tmp_df[(tmp_df['subject_type'] == 'doc') & (tmp_df['subject_doc_id'] == doc_id)]['visitor_country']
        if column.empty:
            return pd.Series([])

        val_count = column.value_counts()

        if (plot):
            self._plot_frequency_table(
                val_count,
                y_label="Users' countries", 
                x_label="Value count of each country",
                title=f"Horizontal bar chart of the number of occurency the countries of the user consulting the doc {doc_id}"

            )
        
        return val_count

    def view_by_continent(self, doc_id, plot=True):
        """Implements the view by continent functionality"""
        if (doc_id is None):
            raise IncorrectInputDataException()

        val_count_by_country = pd.DataFrame(self.view_by_country(doc_id, plot = False))
        
        if (val_count_by_country.empty == False):

            # converts the index column into a common column
            val_count_by_country["country"] = val_count_by_country.index

            # converts the country column into a continent column
            val_count_by_country['continent'] = val_count_by_country["country"].apply(lambda x: None if x not in self.COUNTRY_TO_CONTINENT_MAPPING.keys() else self.COUNTRY_TO_CONTINENT_MAPPING[x])

            # groupby these continent columns and sum their values of visitor_country (counting visitor per country)
            val_count = val_count_by_country.groupby('continent')['visitor_country'].sum()

            if (plot):
                self._plot_frequency_table(
                    val_count,
                    y_label="Users' countries", 
                    x_label="Value count of each country",
                    title=f"Horizontal bar chart of the number of occurency the countries of the user consulting the doc {doc_id}"

                )
            
            return val_count

        else:
            return val_count_by_country

    def also_likes(self, doc_id, user_id = None, plot=True):
        """Implements the also likes functionality"""
        if (doc_id is None):
            raise IncorrectInputDataException()



        visitors = self._readers_of(doc_id)

        # Not to output the documents read by the current user
        if user_id is not None:
            if self.user_id_exists(user_id) == False:
                user_id = None
            else:
                visitors = visitors[visitors["visitor_uuid"] != user_id]

        # There is a high probability of finding duplicates as documents read by similar visitors tend to be the same        
        visitors["docs"] = visitors["visitor_uuid"].apply(lambda vis_id: self._has_read(vis_id).values.flatten())

        documents = visitors["docs"]

        if (documents.size == 0):
            #print("Document not found...")
            return np.array([])

        else:

            list_of_docs = np.concatenate(documents.values).ravel()

            # We then sort the result by frequency of apparition of the documents
            
            list_of_docs = np.delete(list_of_docs, np.where(list_of_docs == doc_id))

            unique_docs, counts = np.unique(list_of_docs, return_counts=True)
            sorted_index = np.argsort(-counts)
            unique_docs_sorted = unique_docs[sorted_index]

            if (plot):
                also_likes_graph = Digraph(comment="Also-Likes")

                # First adding the users
                also_likes_graph.attr('node', shape="box")

                if user_id is not None:
                    also_likes_graph.node(user_id[-4:], style="filled", fillcolor="forestgreen", color="forestgreen")

                for user in visitors["visitor_uuid"]:
                    also_likes_graph.node(user[-4:])

                # Then adding the docs
                also_likes_graph.attr('node', shape="ellipse")

                also_likes_graph.node(doc_id[-4:], style="filled", fillcolor="forestgreen", color="forestgreen")

                for doc in unique_docs_sorted:
                    if doc != doc_id:
                        also_likes_graph.node(doc[-4:])

                if user_id is not None:
                    # Adding current user/doc relation
                    also_likes_graph.edge(user_id[-4:], doc_id[-4:])

                def create_relations(row):

                    visitor, docs = row[0], row[1]

                    for doc in docs:
                        also_likes_graph.edge(visitor[-4:],doc[-4:])

                # Now adding the relations
                visitors[["visitor_uuid","docs"]].apply(create_relations, axis = 1)

                print("saving to dot format..")
                also_likes_graph.save("also_likes.dot")
                print("converting dot format to image..")
                # system call to the executable

                if (platform.system() == "Windows"):
                    executable_path = os.path.join(os.getcwd(), self._GRAPHVIZ_W_BIN_PATH)
                    os.system(f"{os.path.join(executable_path,'dot.exe')} -Tjpeg -o also_likes.jpeg also_likes.dot")
                else:
                    # We expect Graphviz to be installed. If not, use 'sudo apt-get install graphviz'
                    also_likes_graph.render("also_likes.ps")

            # returns the top 10
            return unique_docs_sorted[:10]