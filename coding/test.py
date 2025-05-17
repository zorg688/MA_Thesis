import numpy as np

import pandas as pd

test_dict = {"Row1": [("test", "test2"), "test3"], "Row2": ["Test"]}

test_output = pd.DataFrame.from_dict(test_dict, orient = "index")

print(f"This is a test: \n{test_output}")