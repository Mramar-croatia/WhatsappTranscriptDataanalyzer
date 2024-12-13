import pandas as pd
import matplotlib.pyplot as plt

text_x_offset = 0.20
text_y_offset = 5
rotation = 0

def count_hours(messages):
    hour_dict = {
        'hour': [],
        'number_of_messages': []
    }

    for i in range(0, 24):
        hour_dict['hour'].append(str(i).rjust(2, '0'))
        hour_dict['number_of_messages'].append(0)

    messages = messages.reset_index(drop=True)

    for index, row in messages.iterrows():
        # print(row['timestamp'][12:14].rjust(2, '0'))
        hour_dict['number_of_messages'][hour_dict['hour'].index(row['timestamp'][12:14].rjust(2, '0'))] += 1

    for i in range(len(hour_dict['hour'])):
        hour_dict['hour'][i] = str(int(hour_dict['hour'][i])) + ':00'
        
    hours = pd.DataFrame(hour_dict)

    hours = hours.set_index('hour')
    
    return hours

def plot_hour_count(hours):
    colors = ['skyblue', 'purple', 'gray']

    plt.figure(figsize=(40, 20))
    bars = plt.bar(hours.index, hours['number_of_messages'],  color=colors[:len(hours)])
    plt.xlabel('Hour', fontsize=30, labelpad=40)  # Increase font size and set label padding for x-axis label
    plt.ylabel('Number of messages', fontsize=30, labelpad=50)  # Increase font size and set label padding for y-axis label
    plt.title('Number of messages sent each hour', fontsize=40, pad=50)  # Increase font size and set title padding

    # Increase font size for x-axis and y-axis ticks
    plt.xticks(fontsize=15, rotation=rotation)
    plt.yticks(fontsize=15)

    # Add value annotations on top of the bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2 - text_x_offset, bar.get_height() + text_y_offset, str(int(bar.get_height())),
                fontsize=20, color='black')
        
    plt.savefig('./RESULTS/hours.png', bbox_inches='tight')

    # plt.show()
    
def process_hour_count(messages):
    plot_hour_count(count_hours(messages))