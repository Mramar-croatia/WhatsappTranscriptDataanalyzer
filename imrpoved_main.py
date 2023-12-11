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
    output_path = fd.askopenfilename()

    modify_transcript(input_path, output_path)


data_dict = {'age': [20, 20, 21, 20, 21, 20],
             'math_marks': [1, 90, 91, 98, 92, 95],
             'physics_marks': [90, 100, 91, 92, 98, 95],
             'chem_marks': [93, 89, 99, 92, 94, 92]
             }

df = pd.DataFrame(data_dict, index=['Marko', 'Jana', 'Sara', 'Fara', 'Klara', 'Maja'])

plot = df.plot.pie(y='math_marks', figsize=(10, 10), fontsize = 12)

plt.title('Math plot')

plt.show()

print(df)