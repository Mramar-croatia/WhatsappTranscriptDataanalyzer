import numpy as np
import pandas as pd


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
