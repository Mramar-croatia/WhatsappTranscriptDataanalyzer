from tkinter import Tk
from tkinter import filedialog as fd

import numpy as np
import pandas as pd

from functions import *


def process_transcript():
    root = Tk()
    root.withdraw()

    input_path = fd.askopenfilename()
    output_path = fd.askopenfilename()

    modify_transcript(input_path, output_path)


lst = ["ja", "Ba", "ja"]
df = pd.DataFrame(lst)
print(df)