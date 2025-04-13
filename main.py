from tkinter import Tk
from tkinter import filedialog as fd

from analysis_functions.date_functions import *
from analysis_functions.user_functions import *
from analysis_functions.word_functions import *
from analysis_functions.load_functions import *
from analysis_functions.media_functions import *
from analysis_functions.hour_functions import *
from analysis_functions.emoji_functions import *

if __name__ == '__main__':
    root = Tk()
    root.withdraw()

    input_path = fd.askopenfilename()
    # input_path = './WhatsAppChat.txt'

    messages_df = to_pandas(input_path)
    
    process_common_emojis(messages_df)
    process_common_words(messages_df)
    process_user_message_count(messages_df)
    process_user_media_count(messages_df)
    process_date_distribution(messages_df)
    write_general_data(messages_df)
    process_hour_count(messages_df)
    