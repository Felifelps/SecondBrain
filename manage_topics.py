"""
# Auto topics generator

This file generates a topics list on each .md file on a directory

The sintax to use is:

    `python manage_topics.py <directory> -r`

    directory: The dir with the .md files.
    -r (optional): Removes the topics list instead of adding

    `python manage_topics.py -a -r`

    -a: Stands for "all". Mades the process to all the dirs
    -r (optional): Removes the topics list instead of adding

    `python manage_topics.py -h`

    -h: Stands for "help". Show this message
"""

import re
import os
import sys

TOPICS_TITLE = '## Tópicos'
TOPIC_PATTERN = '## .*\n'

IGNORE_DIRS = ".venv", "__pycache__", ".git", "img"
DOCSTRING = __doc__

ERROR_MESSAGE = '\nError: {}\nTry "python manage_topics.py -h" for help with the sintax\n'

def generate_slug(string: str):
    forbidden_chars = '.?'
    for char in forbidden_chars:
        string = string.replace(char, '')
    return string.lower().replace(' ', '-')


def write_result(data, *path_components):
    path = os.path.join(*path_components)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(data)


def manage_topics_on_file(file_path, only_remove):
    # Getting text from file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    result = re.findall(TOPIC_PATTERN, data)

    # If topics already exists, remove then
    if TOPICS_TITLE in data:
        # Remove it from the topics
        result.pop(0)

        # Gets the start of the topics list
        start_pos = data.index(TOPICS_TITLE)

        # Gets the start of the first topic (end of the topics list)
        final_pos = data.index(result[0])

        data = data[:start_pos] + data[final_pos:]

    if not result:
        return None

    if not only_remove:

        topics_list = f'{TOPICS_TITLE}'

        for topic in result:
            topic = topic[3:].strip()
            slug = generate_slug(topic)
            topics_list += f'\n- [{topic}](#{slug})'

        topics_list += '\n\n'

        pos = data.index(result[0])

        data = data[:pos] + topics_list + data[pos:]

    write_result(data, file_path)

def manage_topic_on_dir_files(directory, only_remove):
    if not os.path.exists(directory):
        raise Exception(f'{directory} directory not found')

    print(f'Looking into {directory}...')

    files = list(os.walk(directory))[0][-1]

    # Removing README.md
    if 'README.md' in files:
        files.pop(files.index('README.md'))

    for file in files:
        print(f' - Processing {file}... ', end='')
        manage_topics_on_file(os.path.join(directory, file), only_remove)
        print('Done')

def main():
    args = sys.argv
    only_remove = '-r' in args
    try:
        if '-h' in args:
            return print(DOCSTRING)

        # -a stands for "all or auto"
        if '-a' in args:
            print('Adding topics to all directories')

            # Gets the current dir data, and gets the subdirs
            current_dir = list(os.walk(os.getcwd()))[0]
            for directory in current_dir[1]:
                if directory not in IGNORE_DIRS:
                    manage_topic_on_dir_files(
                        directory, only_remove
                    )

            return print('All directories files updated successfully!')

        # Getting the base dir
        directory = args[1].replace('\\', '')

        manage_topic_on_dir_files(
            directory, only_remove
        )

    except IndexError:
        print(ERROR_MESSAGE.format('Sintax error'))
        sys.exit(1)
    except Exception as e:
        print(ERROR_MESSAGE.format(str(e)))
        sys.exit(1)

if __name__ == "__main__":
    main()
