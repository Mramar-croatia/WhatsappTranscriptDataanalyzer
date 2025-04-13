import matplotlib.pyplot as plt
import pandas as pd

from datetime import datetime

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

    earliest = to_ymd_date(messages.iloc[0]['timestamp'])

    for i in pd.date_range(start=earliest,end=to_ymd_date(messages.iloc[-1]['timestamp'])):
        date_dict['date'].append(to_dmy_date(str(i)[:10]))
        date_dict['number_of_messages'].append(0)

    messages = messages.reset_index(drop=True)

    for index, row in messages.iterrows():
        if to_dmy_date(to_ymd_date(row['timestamp'])) in date_dict['date']:
            date_dict['number_of_messages'][date_dict['date'].index(to_dmy_date(to_ymd_date(row['timestamp'])))] += 1  

    dates = pd.DataFrame(date_dict)

    dates = dates.set_index('date')

    return dates

def plot_date_dataframe(df):
    plt.figure(figsize=(20, 10))
    plt.plot(df.index, df['number_of_messages'])
    
    # Set the x-ticks to show every 10th tick
    num_ticks = len(df.index)
    if num_ticks > 10:  # Check if there are enough ticks to show
        plt.xticks(ticks=range(0, num_ticks, 14), labels=map(lambda x: str(x).replace('-', '.'), df.index[::14]), rotation=-80)
    else:
        plt.xticks(rotation=-80)  # Default behavior if there are fewer than 10 ticks
    
    plt.title('Date distribution of messages')
    plt.savefig('./RESULTS/date_distribution.png', bbox_inches='tight')
    # plt.show()
    
def process_date_distribution(message_dataframe):
    dates = GenerateDateFrame(message_dataframe)
    plot_date_dataframe(dates)
    sorted_dates = dates.sort_values(by='number_of_messages', ascending=False)
    with open('./RESULTS/date_distribution.txt', 'w') as f:
        f.write(sorted_dates.to_string())