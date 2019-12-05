# libraries import
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Frame, Button, Entry, Style

# local files import
from classes.abstract.AbstractGUI import AbstractGUI


class IssuuGUI(AbstractGUI):
    """Holds the GUI of an Issuu-syntaxed dataset"""

    def __init__(self, operator, doc_uid, user_uid):
        """Operator has to be of type IssuuOperator."""
        super().__init__(operator)

        # UI related initilizations
        self.root = Tk()

        self.str_var_doc_uid = StringVar()
        if doc_uid == None:
            self.str_var_doc_uid.set("No value specified")
        else:
            self.str_var_doc_uid.set(doc_uid)
            
        self.str_var_user_uid = StringVar()
        if user_uid == None:
            self.str_var_user_uid.set("No value specified")
        else:
            self.str_var_user_uid.set(user_uid)

        self._initUI()




    def _initUI(self):
        """This method also deals with the design of the GUI"""

        def view_by_country_continent(doc_id, country=True):
            print(doc_id)
            if self.operator.doc_id_exists(doc_id):
                if (country):
                    return self.operator.view_by_country(doc_id)
                else:
                    return self.operator.view_by_continent(doc_id)
            else:
                self._open_error_popup("Doc id not found !")

        def view_by_browser(pretty=False):
                return self.operator.view_by_browser(simplified=pretty)

        def also_likes(doc_id, user_uid, graph=True):
            if self.operator.doc_id_exists(doc_id):
                res = self.operator.also_likes(doc_id, user_uid, plot=graph)
                if (graph):
                    self._open_error_popup("Graph generated in file 'also_like.jpeg'",title="Graph Generated")
                else:
                    text = ""
                    for i, line in enumerate(res):
                        text+= f"{i}: {line}\n"
                    self._open_error_popup(text, title="Also-Likes document")
            else:
                self._open_error_popup("Doc id not found !")

        self.root.geometry("480x320")

        self.mainframe = Frame(self.root, width=480, height=320, relief = 'raised', borderwidth=5)

        self.mainframe.master.title("IssuuGUI")
        
        Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

        buttons_info = [
            {"text": "View by Country", 'action': lambda : view_by_country_continent(self.str_var_doc_uid.get(), country=True)},
            {"text": "View by Continent", 'action': lambda : view_by_country_continent(self.str_var_doc_uid.get(), country=False)},
            {"text": "View by Browser (dirty)", 'action': lambda : view_by_browser(pretty=False)},
            {"text": "View by Browser (clean)", 'action': lambda : view_by_browser(pretty=True)},
            {"text": "Also-Likes list", 'action': lambda : also_likes(self.str_var_doc_uid.get(), self.str_var_user_uid.get(), graph=False)},
            {"text": "Also-Likes graph", 'action': lambda : also_likes(self.str_var_doc_uid.get(), self.str_var_user_uid.get(), graph=True)},
        ]

        labels_input = [
            Label(self.mainframe, text="Dataset: "+self.operator.get_dataset_path()),
            Label(self.mainframe, text="User uid:"),
            Entry(self.mainframe, textvariable=self.str_var_user_uid),
            Label(self.mainframe, text="Doc uid:"),
            Entry(self.mainframe, textvariable=self.str_var_doc_uid)
        ]

        # 2 columns configured
        self.mainframe.columnconfigure(0, weight=1, pad=3)
        self.mainframe.columnconfigure(1, weight=1, pad=3)

        # 6 rows configured
        for i in range(0,7):
            self.mainframe.rowconfigure(i, weight=1,pad=3)
        

        # leftFrame = Frame(self.mainframe)
        # leftFrame.grid(rowspan=, column = 0, sticky = W+E+N+S)
        
        # Adding content of the left column
        for i, cnt in enumerate(labels_input):
            cnt.grid(row=i, column=0, sticky="ew")

        # Adding button of the right column
        for i, button in enumerate(buttons_info):
            btn = Button(self.mainframe, text=button["text"], command=button['action'])
            btn.grid(row=i, column=1, sticky="ew")

        self.mainframe.grid(sticky='nswe')
        self.mainframe.rowconfigure(0)
        self.mainframe.columnconfigure(0)
        self.mainframe.grid_propagate(0)

        self.mainframe.pack()

    def _open_error_popup(self, message, title="Error"):
        win = Toplevel()
        win.wm_title(title)

        l = Label(win, text=message)
        l.grid(row=0, column=0)

        b = Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)

    def show(self):
        self.root.mainloop()
        