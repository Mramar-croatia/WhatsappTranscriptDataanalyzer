import matplotlib.pyplot as plt
import pandas as pd

text_x_offset = 0.24
text_y_offset = 50
rotation = 0

def count_common_words(messages):
    # Assuming you have a DataFrame named 'messages'
    all_messages = ' '.join(messages['contents'].astype(str).str.lower())

    # Split the text into words
    words = all_messages.split()

    # Create a DataFrame with word counts
    word_counts = pd.Series(words).value_counts().reset_index()
    word_counts.columns = ['word', 'count']

    # Remove unwanted words
    unwanted_words = ['<media', 'omitted>']
    word_counts = word_counts[~word_counts['word'].isin(unwanted_words)]

    # Set 'word' as the index
    word_counts.set_index('word', inplace=True)

    # Reset index to keep 'word' as a column and not index
    word_counts.reset_index()

    # Display the top 20 most common words
    top_words = word_counts.head(60)
    
    return top_words

def plot_common_words(top_words):
    # Manually specify colors for each user
    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

    plt.figure(figsize=(40, 20))
    bars = plt.bar(top_words.index, top_words['count'],  color=colors[:len(top_words)])
    plt.xlabel('Word', fontsize=30, labelpad=40)  # Increase font size and set label padding for x-axis label
    plt.ylabel('Number of usages', fontsize=30, labelpad=50)  # Increase font size and set label padding for y-axis label
    plt.title('Number of times each Word was used', fontsize=40, pad=50)  # Increase font size and set title padding

    # Increase font size for x-axis and y-axis ticks
    plt.xticks(fontsize=16, rotation=rotation)
    plt.yticks(fontsize=15)

    # Add value annotations on top of the bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2 - text_x_offset, bar.get_height() + text_y_offset, str(int(bar.get_height())),
                fontsize=20, color='black')
        
    plt.savefig('./RESULTS/word_distribution.png', bbox_inches='tight')

    # plt.show()
    
def process_common_words(message_dataframe):
    top_words = count_common_words(message_dataframe)
    plot_common_words(top_words)