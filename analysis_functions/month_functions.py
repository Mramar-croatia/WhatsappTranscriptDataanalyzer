from tkinter import font
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.cm as cm

def to_ymd_date(timestamp):
    day = timestamp[0:2]
    month = timestamp[3:5]
    year = timestamp[6:10]
    return f'{year}-{month}-{day}'

def GenerateMonthlyFrame(messages):
    messages = messages.copy()
    messages['date'] = pd.to_datetime(messages['timestamp'].apply(to_ymd_date), format='%Y-%m-%d')
    messages['month'] = messages['date'].dt.to_period('M').astype(str)

    monthly_counts = messages.groupby('month').size().reset_index(name='number_of_messages')
    monthly_counts = monthly_counts.set_index('month')

    return monthly_counts

def plot_monthly_dataframe(df):
    plt.figure(figsize=(20, 10))

    # Create a unique color for each bar
    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

    # Create the bar plot
    bars = plt.bar(df.index, df['number_of_messages'], color=colors)

    # Annotate each bar with the message count
    for bar, count in zip(bars, df['number_of_messages']):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(count),
                 ha='center', va='bottom', fontsize=15)

    # Customize ticks
    plt.xticks(ticks=range(len(df.index)), labels=df.index, rotation=-80, fontsize=18)

    plt.title('Monthly distribution of messages', fontsize=40, pad=20)
    plt.xlabel('Month', fontsize = 35, labelpad=20)
    plt.ylabel('Number of Messages', fontsize = 35, labelpad=20)
    plt.tight_layout()
    plt.savefig('./RESULTS/monthly_distribution.png', bbox_inches='tight')
    # plt.show()


def process_monthly_distribution(message_dataframe):
    monthly = GenerateMonthlyFrame(message_dataframe)
    plot_monthly_dataframe(monthly)
    sorted_months = monthly.sort_values(by='number_of_messages', ascending=False)
    with open('./RESULTS/monthly_distribution.txt', 'w') as f:
        f.write(sorted_months.to_string())
