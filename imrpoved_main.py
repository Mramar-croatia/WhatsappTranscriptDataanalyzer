from tkinter import Tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from functions import *

'''
df = pd.DataFrame(data_dict)
df = df.set_index ('name')
plot = df.plot.pie(y='math_marks', figsize=(10, 10), fontsize = 12)
plt.title('Math plot')
plt.show()
print(df)
'''

messages_df = process_transcript_to_pandas()

'''
dates_dataframe = GenerateDateFrame(messages_df)

plt.figure()

tk = dates_dataframe.plot(figsize=(30,30)).get_figure()

tk.savefig('test.pdf')
'''

count_user_messages(messages_df)

