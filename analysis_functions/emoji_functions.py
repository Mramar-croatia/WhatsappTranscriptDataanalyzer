import matplotlib.pyplot as plt
import pandas as pd
import re
from matplotlib import rcParams

rcParams['font.family'] = 'Segoe UI Emoji'  # Windows

emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U00002700-\U000027BF"
    "\U0001F900-\U0001F9FF"
    "\U00002600-\U000026FF"
    "]+", flags=re.UNICODE
)

def count_emojis_by_user(messages, user_column='sender', text_column='contents'):
    all_emojis = []

    for _, row in messages.iterrows():
        sender = row[user_column]
        text = str(row[text_column])
        for char in text:
            if emoji_pattern.fullmatch(char):
                all_emojis.append({'emoji': char, 'user': sender})

    df = pd.DataFrame(all_emojis)

    if df.empty:
        return pd.DataFrame()

    emoji_user_counts = df.groupby(['emoji', 'user']).size().reset_index(name='count')
    total_counts = df['emoji'].value_counts().head(30).reset_index()
    total_counts.columns = ['emoji', 'total']

    return emoji_user_counts, total_counts

def plot_stacked_emoji_usage(emoji_user_counts, total_counts):
    if emoji_user_counts.empty:
        print("No emojis found.")
        return

    pivot = emoji_user_counts.pivot(index='emoji', columns='user', values='count').fillna(0)

    ordered_emojis = total_counts['emoji'].tolist()
    pivot = pivot.loc[ordered_emojis]

    users = pivot.columns
    bottom = [0] * len(pivot)

    plt.figure(figsize=(len(pivot) * 1.0, 10))

    colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'brown', 'gray']

    for i, user in enumerate(users):
        plt.bar(pivot.index, pivot[user], bottom=bottom, label=user, color=colors[i % len(colors)])
        bottom = [b + u for b, u in zip(bottom, pivot[user])]

    for i, emoji in enumerate(pivot.index):
        total = pivot.loc[emoji].sum()
        plt.text(
            i,                    # x position (bar index)
            total + 0.5,          # y position (slightly above the bar)
            str(int(total)),      # the text (total count)
            ha='center',
            va='bottom',
            fontsize=18
        )

    plt.xlabel('Emoji', fontsize=30, labelpad=20)
    plt.ylabel('Number of usages', fontsize=30, labelpad=30)
    plt.title('Most Common Emojis Used (by user)', fontsize=40, pad=30)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=20)
    plt.savefig('./RESULTS/emoji_distribution.png', bbox_inches='tight')


def process_common_emojis(message_dataframe):
    emoji_user_counts, total_counts = count_emojis_by_user(message_dataframe)
    plot_stacked_emoji_usage(emoji_user_counts, total_counts)