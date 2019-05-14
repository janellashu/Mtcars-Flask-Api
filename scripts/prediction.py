#!/usr/bin/env python3

import pandas as pd
from statsmodels.formula.api import ols

data = pd.read_csv("../scripts/mtcars.csv")
#data['vs'] = data['vs'].astype('category', copy = False)
#data['am'] = data['am'].astype('category', copy = False)

model = ols('mpg ~ wt + qsec + am', data).fit()

def predict(dict_values,model=model):
    col_label = ["wt", "qsec", "am"]
    x1 = [float(dict_values[col]) for col in col_label]
    x = pd.DataFrame(x1, col_label).T
    y_pred = float(model.predict(x))
    return y_pred
