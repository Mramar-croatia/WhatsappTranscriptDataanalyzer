from tkinter import Tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from functions import *

messages_df = process_transcript_to_pandas()

count_user_messages(messages_df)