from classes.ISSUU.IssuuFactory import IssuuFactory

if __name__ == "__main__":
    fact = IssuuFactory()
    ds = fact.load_dataset("gibberish.json")