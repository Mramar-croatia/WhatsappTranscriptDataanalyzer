import pandas as pd

# Takes a string, returns a pandas dataframe
def to_pandas(input_filepath):
    # Loads the text into a list
    with open(input_filepath, 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    if ':' not in lines[0][20:]:
        lines.remove(lines[0])

    # chat_name = input_filepath[input_filepath.rfind('WhatsApp Chat'):]
    chat_name = input('Name of the chat: ')

    return pd.DataFrame(transcript_to_dictionary(lines))

def transcript_to_dictionary(lines):

    message_dict = {
        'timestamp': [],
        'sender': [],
        'contents': []
    }

    current_message = ['timestamp', 'sender', 'contents']

    for line in lines:
        if len(line) >= 19 and line[18] == '-':
            # take the timestamp
            current_message[0] = line[0:17]
        
            # take the rest of the message
            line = line[20:]
            
            if ':' in line:
                # take the sender
                current_message[1] = line[0:line.index(':')]
                
                # take the contents
                current_message[2] = line[line.index(':')+2:]
                
                message_dict['timestamp'].append(current_message[0])
                message_dict['sender'].append(current_message[1])
                message_dict['contents'].append(current_message[2].rstrip('\n'))
        else:
            current_message[2] += line

      
    if message_dict['contents'][-1] != current_message[2]:    
        message_dict['timestamp'].append(current_message[0])
        message_dict['sender'].append(current_message[1])
        message_dict['contents'].append(current_message[2])

    return message_dict