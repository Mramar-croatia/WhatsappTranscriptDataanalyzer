import matplotlib.pyplot as plt
import pandas as pd

text_x_offset = 0.35
text_y_offset = 50
rotation = -80

min_message = 500
# min_message = int(input('Minimal message treshold: '))

def count_user_messages(message_dataframe):
    
    user_message_counts = message_dataframe['sender'].value_counts().reset_index()
    user_message_counts.columns = ['sender', 'message_count']
    
    user_message_counts = user_message_counts[user_message_counts['message_count'] >= min_message]
    
    user_message_count_df = pd.DataFrame(user_message_counts)
    
    return user_message_count_df

    
def plot_user_message_count(user_message_count_df):
    # Manually specify colors for each user
    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

    plt.figure(figsize=(40, 20))
    bars = plt.bar(user_message_count_df['sender'], user_message_count_df['message_count'],  color=colors[:len(user_message_count_df)])
    plt.xlabel('Sender', fontsize=30, labelpad=40)  # Increase font size and set label padding for x-axis label
    plt.ylabel('Number of messages', fontsize=30, labelpad=50)  # Increase font size and set label padding for y-axis label
    plt.title('Number of messages per person', fontsize=40, pad=50)  # Increase font size and set title padding

    # Increase font size for x-axis and y-axis ticks
    plt.xticks(fontsize=15, rotation=rotation)
    plt.yticks(fontsize=15)

    # Add value annotations on top of the bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2 - text_x_offset, bar.get_height() + text_y_offset, str(int(bar.get_height())),
                fontsize=20, color='black')

    # Save the plot as an image file
    plt.savefig('./RESULTS/user_count.png', bbox_inches='tight')
    
    # plt.show()
    
def process_user_message_count(message_dataframe):
    user_message_count_df = count_user_messages(message_dataframe)
    plot_user_message_count(user_message_count_df)