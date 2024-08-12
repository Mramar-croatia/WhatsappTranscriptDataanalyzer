from tkinter import Tk
from tkinter import filedialog as fd

from analysis_functions.date_functions import *
from analysis_functions.user_functions import *
from analysis_functions.word_functions import *
from analysis_functions.load_functions import *

root = Tk()
root.withdraw()

input_path = fd.askopenfilename()
# input_path = './WhatsAppChat.txt'

messages_df = to_pandas(input_path)