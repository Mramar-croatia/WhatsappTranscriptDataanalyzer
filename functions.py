import numpy as np
import pandas as pd

from datetime import datetime


def to_pandas(input_filepath):
    # Loads the text into a list
    with open(input_filepath, 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    if ':' not in lines[0][20:]:
        lines.remove(lines[0])

    chat_name = input_filepath[input_filepath.rfind('WhatsApp Chat'):]

    message_dict = transcript_to_dictionary(chat_name, lines)

    return pd.DataFrame(message_dict)


def transcript_to_dictionary(chat_name, lines):

    message_dict = {
        'timestamp': [],
        'chat_name': [],
        'sender': [],
        'contents': []
    }

    current_message = ['timestamp', 'chat_name', 'sender', 'contents']

    current_message[0] = lines[0][:17]
    line = lines[0][20:]
    current_message[1] = chat_name
    current_message[2] = line[:line.find(':')]
    line = line[line.find(':') + 2:]
    current_message[3] = line

    lines.remove(lines[0])

    for line in lines:
        if len(line) > 19 and line[2] == '/' and ':' in line[20:]:
            message_dict['timestamp'].append(current_message[0])
            message_dict['chat_name'].append(current_message[1])
            message_dict['sender'].append(current_message[2])
            message_dict['contents'].append(current_message[3])

            current_message = ['timestamp', 'chat_name', 'sender', 'contents']

            current_message[0] = line[:17]
            line = line[20:]

            current_message[1] = chat_name

            current_message[2] = line[:line.find(':')]
            line = line[line.find(':') + 2:]

            current_message[3] = line

        else:
            current_message[3] += line

    message_dict['timestamp'].append(current_message[0])
    message_dict['chat_name'].append(current_message[1])
    message_dict['sender'].append(current_message[2])
    message_dict['contents'].append(current_message[3])

    return message_dict


def to_ymd_date (timestamp):
    day = timestamp[0:2]
    month = timestamp[3:5]
    year = timestamp[6:10]
    return f'{year}-{month}-{day}'

def to_dmy_date (timestamp):
    day = timestamp[8:10]
    month = timestamp[5:7]
    year = timestamp[:4]
    return f'{day}-{month}-{year}'


def GenerateDateFrame(messages):
    # Zoome time

    date_dict = {
        'date': [],
        'number_of_messages': []
    }

    starting_date = '12/11/2022'
    earliest = to_ymd_date(messages.iloc[0]['timestamp'])

    for i in pd.date_range(start='12/11/2022',end=to_ymd_date(messages.iloc[-1]['timestamp'])):
        date_dict['date'].append(to_dmy_date(str(i)[:10]))
        date_dict['number_of_messages'].append(0)

    messages = messages.reset_index(drop=True)

    for index, row in messages.iterrows():
        if to_dmy_date(to_ymd_date(row['timestamp'])) in date_dict['date']:
            date_dict['number_of_messages'][date_dict['date'].index(to_dmy_date(to_ymd_date(row['timestamp'])))] += 1  

    dates = pd.DataFrame(date_dict)

    dates = dates.set_index('date')

    dates = dates.sort_values("number_of_messages", ascending=True)

    return dates