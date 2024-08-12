import pandas as pd
import matplotlib.pyplot as plt

text_x_offset = 0.24
text_y_offset = 2
rotation = -80

min_media = 50
# min_media = int(input('Minimal media treshold: '))

def user_count_media(messages):

    # Assuming your dataframe is named df
    substrings_to_keep = ['null', '<Media omitted>']

    # Create a condition for each substring and combine them with the logical OR operator
    condition = messages['contents'].str.contains('|'.join(substrings_to_keep))

    # Filter rows where the 'contents' column contains any of the specified substrings
    messages = messages[condition]
    
    messages = messages.reset_index()
    
    

    user_media_counts = messages['sender'].value_counts().reset_index()
    user_media_counts.columns = ['sender', 'message_count']
    
    user_media_counts = user_media_counts[user_media_counts['message_count'] >= min_media]
    
    user_media_df = pd.DataFrame(user_media_counts)
    
    return user_media_df

def plot_user_media_count(user_media_df):
    # Manually specify colors for each user
    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

    plt.figure(figsize=(40, 20))
    bars = plt.bar(user_media_df['sender'], user_media_df['message_count'],  color=colors[:len(user_media_df)])
    plt.xlabel('Sender', fontsize=30, labelpad=40)  # Increase font size and set label padding for x-axis label
    plt.ylabel('Number of messages', fontsize=30, labelpad=50)  # Increase font size and set label padding for y-axis label
    plt.title('Number of messages with media attachemnts per person', fontsize=40, pad=50)  # Increase font size and set title padding

    # Increase font size for x-axis and y-axis ticks
    plt.xticks(fontsize=15, rotation=rotation)
    plt.yticks(fontsize=15)

    # Add value annotations on top of the bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2 - text_x_offset, bar.get_height() + text_y_offset, str(int(bar.get_height())),
                fontsize=30, color='black')
        
    plt.savefig('./RESULTS/user_media_count.png', bbox_inches='tight')

    # plt.show()
    
def process_user_media_count(media_dataframe):
    plot_user_media_count(user_count_media(media_dataframe))