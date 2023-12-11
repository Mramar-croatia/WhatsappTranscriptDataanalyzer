from tkinter import Tk
from tkinter import filedialog as fd


def modify_transcript(input_filepath, output_filepath):
    # Loads the text into a list
    with open(input_filepath, 'r', encoding="utf8") as f:
        original_lines = f.readlines()
        f.close()

    # For modifying lines in the input
    modified_lines = []

    # For keeping track of the people in the conversation
    name_list = []

    # For keeping track of how many media has gone through the conversation
    media_tracker = 0

    for line in original_lines:
        # Remove the time stamp, try is needed for if there is no index 2
        try:
            if line[2] == '/':
                line = line[20:]
        except:
            line = line

        # If the line is a beginning of a new message
        if ':' in line and line.index(':') <= 25:
            s = ''

            # Filip (ne Gasparovic lol)
            for i in line[:line.index(':')].split():
                s += i.replace('(', '')[0]

            # Save the name to the name list if it is not already there and there are not too many names
            if f'{line[:line.index(':')]} - {s}\n' not in name_list and len(name_list) <= 12:
                name_list.append(f'{line[:line.index(':')]} - {s}\n')

            s += line[line.index(':'):]
            line = s

        # Removes the media
        if '<Media omitted>' in line:
            line = line.replace('<Media omitted>', '<M>')
            media_tracker += 1

        modified_lines.append(line)

    # Add separation
    name_list.append('\n')

    with open(output_filepath, 'w', encoding="utf8") as f:
        f.writelines(name_list)
        f.writelines(modified_lines)
        f.write(f'\n{media_tracker} media files have passed trough this conversation')


root = Tk()
root.withdraw()

input_path = fd.askopenfilename()
output_path = fd.askopenfilename()

modify_transcript(input_path, output_path)