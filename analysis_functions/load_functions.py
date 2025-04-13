import pandas as pd

# Takes a string, returns a pandas dataframe
def to_pandas(input_filepath):
    # Loads the text into a list
    with open(input_filepath, 'r', encoding="utf8") as f:
        lines = f.readlines()
        f.close()

    if ':' not in lines[0][20:]:
        lines.remove(lines[0])

    return pd.DataFrame(transcript_to_dictionary(lines))

def transcript_to_dictionary(lines):

    message_dict = {
        'timestamp': [],
        'sender': [],
        'contents': []
    }

    current_message = ['timestamp', 'sender', 'contents']

    for line in lines:
        if len(line) >= 19 and line[17:20] == ' - ':
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

def remove_media(message_dataframe):
    for i in range(len(message_dataframe['contents'])):
        if '<Media omitted>' in message_dataframe['contents'][i] or '<media omitted>' in message_dataframe['contents'][i]:
            message_dataframe['contents'][i] = ''
            
    return message_dataframe

def write_general_data(message_dataframe):
    with open('./RESULTS/general_data.txt', 'w', encoding='utf-8') as f:
        f.write('Number of messages: ' + str(len(message_dataframe)) + '\n')
        f.write('Number of senders: ' + str(len(message_dataframe['sender'].unique())) + '\n')
        f.write('Number of words: ' + str(message_dataframe['contents'].apply(lambda x: len(x.split())).sum()) + '\n')
        f.write('Number of characters: ' + str(message_dataframe['contents'].apply(lambda x: len(x)).sum()) + '\n')
        f.write('Average message length: ' + str(message_dataframe['contents'].apply(lambda x: len(x)).mean()) + '\n')
        f.write('Average words per message: ' + str(message_dataframe['contents'].apply(lambda x: len(x.split())).mean()) + '\n')
        f.write('Average messages per sender: ' + str(message_dataframe['sender'].value_counts().mean()) + '\n')
            
        # Calculate and write average message length for each sender
        sender_avg_lengths = message_dataframe.groupby('sender')['contents'].apply(lambda x: x.str.len().mean())
        f.write('\nAverage message length per sender:\n')
        senders = [(sender, avg_length) for sender, avg_length in sender_avg_lengths.items()]
        for sender, avg_length in sorted(senders, key=lambda x: x[1]):
            f.write(f'{sender}: {avg_length:.2f} characters\n')
            
        # Calculate and write total characters sent by each sender
        sender_total_chars = message_dataframe.groupby('sender')['contents'].apply(lambda x: x.str.len().sum())
        f.write('\nTotal characters sent per sender:\n')
        for sender, total_chars in sender_total_chars.items():
            f.write(f'{sender}: {total_chars} characters\n')
            
        f.close()