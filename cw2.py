# libraries imports
import argparse
import time

# local imports
from classes.exception.UnknownInputException import UnknownInputException
from classes.ISSUU.IssuuFactory import IssuuFactory

if __name__ == "__main__":

    # Construct the argument parser
    ap = argparse.ArgumentParser()

    # Add the arguments to the parser
    ap.add_argument("-u", "--user_uuid",
    help="Input for the user UUID")

    ap.add_argument("-d", "--doc_uuid",
    help="Input for the document UUID")

    ap.add_argument("-t", "--task_id", required=True, choices=['2a', '2b', '3a', '3b', '4d', '5', '6'],
    help="""
    Input for the task_id. Can take value in (2a, 2b, 3a, 3b, 4d, 5, 6) where:
     - 2a: Opens an horizontal bar chart of the count of document views by country
     - 2b: Opens an horizontal bar chart of the count of document views by continent
     - 3a: Opens an horizontal bar chart of the count of document views by browser with raw names
     - 3b: Opens an horizontal bar chart of the count of document views by browser with cleaned names
     - 4d: Generates an also-like list from the doc_id and user_id (optional)
     - 5:  Generates an also-likes graph from the doc_id and user_id (optional)
     - 6:  launches the GUI
    
    """)

    ap.add_argument("-f", "--filename", required=True,
    help="Input for the name of the JSON file database")
    
    args = vars(ap.parse_args())    

    print("Creating factory..")
    f = IssuuFactory()
    print("Loading dataset..")
    start = time.time()
    ds = f.load_dataset(path=args["filename"])
    end = time.time()
    print(f"Dataset of {ds.size()} elements loaded in {round(end - start, 4)} seconds..")
    op = f.get_operator(ds)
    print("Operator loaded..")

    if (args["task_id"] == '2a'):
        if (args["doc_uuid"] is not None):
            op.view_by_country(args["doc_uuid"])
        else:
            print("Document ID parameter missing.. Interrupting execution")
    elif (args["task_id"] == '2b'):
        if (args["doc_uuid"] is not None):
            op.view_by_continent(args["doc_uuid"])
        else:
            print("Document ID parameter missing.. Interrupting execution")
    elif (args['task_id'] == '3a'):
        op.view_by_browser()
    elif (args["task_id"] == "3b"):
        op.view_by_browser(simplified=True)
    elif (args["task_id"] == "4d"):
        if (args["doc_uuid"] is not None):
            print(op.also_likes(args["doc_uuid"], args["user_uuid"], plot=False))
        else:
            print("Document ID parameter missing.. Interrupting execution")
    elif (args["task_id"] == "5"):
        if (args["doc_uuid"] is not None):
            op.also_likes(args["doc_uuid"], args["user_uuid"], plot=True)
        else:
            print("Document ID parameter missing.. Interrupting execution")
    elif (args["task_id"] == "6"):
        gui = f.launch_GUI(op, args["doc_uuid"], args["user_uuid"])
        print("Loading gui..")
        gui.show()
    else:
        raise UnknownInputException()