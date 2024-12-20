import pandas as pd
PANDAS_VERSION = "1.5.3"

def test_pandas_version():
    ''' Use an assertion to check the output of pd.__version__ '''
    assert pd.__version__ == PANDAS_VERSION, f"Expected version {PANDAS_VERSION}, but got {pd.__version__}"

if __name__ == "__main__":
    test_pandas_version()
    print("Pandas version is correct!")
