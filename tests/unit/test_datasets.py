# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys
import pytest
import pandas as pd

def test_load_data():
    data_path = "./data/sp500_monthly_prices.csv"
    df = pd.read_csv(data_path)
    #assert not os.path.exists(data_path)
    assert df is not None
    assert df.columns.tolist() == [u'Date', u'Price Value']
   

