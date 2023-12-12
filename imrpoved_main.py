from tkinter import Tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from functions import *


def process_transcript():
    root = Tk()
    root.withdraw()

    input_path = fd.askopenfilename()

    return to_pandas(input_path)


data_dict = {'name': ['Marko', 'Jana', 'Sara', 'Fara', 'Klara', 'Maja'],
             'age': [20, 20, 21, 20, 21, 20],
             'math_marks': [1, 90, 91, 98, 92, 95],
             'physics_marks': [90, 100, 91, 92, 98, 95],
             'chem_marks': [93, 89, 99, 92, 94, 92]
             }

'''
df = pd.DataFrame(data_dict)
df = df.set_index ('name')
plot = df.plot.pie(y='math_marks', figsize=(10, 10), fontsize = 12)
plt.title('Math plot')
plt.show()
print(df)
'''

messages = process_transcript()

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(messages)