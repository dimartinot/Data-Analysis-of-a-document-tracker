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
    help="Input for the task_id. Can take value in (2a, 2b, 3a, 3b, 4d, 5, 6)")

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
        pass
    elif (args["task_id"] == '2b'):
        pass
    elif (args['task_id'] == '3a'):
        op.view_by_browser()
    elif (args["task_id"] == "3b"):
        op.view_by_browser(simplified=True)
    elif (args["task_id"] == "4d"):
        pass
    elif (args["task_id"] == "5"):
        pass
    elif (args["task_id"] == "6"):
        pass
    else:
        raise UnknownInputException()