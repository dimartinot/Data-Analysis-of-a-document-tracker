# UnitTesting/UnitTest.py
# The basic unit testing class

class UnitTest():
    testID = ""
    errors = []
    # Override cleanup() if test object creation allocates non-memory
    # resources that must be cleaned up:
    def cleanup(self): pass
    # Verify a condition is true:
    @staticmethod
    def affirm(condition):
        if(not condition):
            UnitTest.errors.append("failed: " + UnitTest.testID)