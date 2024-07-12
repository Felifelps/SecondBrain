import re
import os
import sys

IGNORE_DIRS = ".venv", "__pycache__", ".git", "img"
DOCSTRING = """
# Auto subtopics generator

This file generates subtopics to the README files that also
has the topics list.

The sintax to use is:
    python subtopics.py <directory> "<subtopic-prefix>"

    - directory: The dir with the README.md file.
    - subtopic-prefix (optional): Sets the prefix for
    the subtopics list. Defaults to "    - "

    OR

    python subtopics.py -a

    - -a: Stands for "all". Mades the process to all the dirs
"""

def generate_slug(string: str):
    forbidden_chars = '.?'
    for char in forbidden_chars:
        string = string.replace(char, '')
    return string.lower().replace(' ', '-')

def add_file_subtopics_list(base, file_name, data, subtopic_prefix):
    topic_pattern = r'&## [^&]*'
    try:
        file_path = os.path.join(base, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_data = file.read().replace('\n', '&&')
            # Change line chars to facilitate search
    except FileNotFoundError:
        print(file_path, 'not found')
        return data
    topics = re.findall(topic_pattern, file_data)

    topics_list = ''
    for topic in topics:
        topic = topic.replace('&## ', '').strip()

        # Generates the title slug
        slug = generate_slug(topic)

        final_link = f'[{topic}]({file_name}#{slug})'
        # Checks if the link is already on data
        if final_link in data:
            continue
        topics_list += f'\n{subtopic_prefix}{final_link}'

    title = re.search(file_name, data)
    title_end_pos = title.span()[1] + 1

    return data[:title_end_pos] + topics_list + data[title_end_pos:]


def write_result(main_file, data):
    with open(main_file, 'w', encoding='utf-8') as file:
        file.write(data)


def process_file_data(base, data, subtopic_prefix):
    file_link_pattern = r'[^\(]*\.md'

    result = re.findall(file_link_pattern, data)
    result.pop(0) # Remove the readme link
    result.pop() # Remove the last link

    for title in result:
        data = add_file_subtopics_list(base, title, data, subtopic_prefix)

    return data

def add_subtopics(base, main_file, subtopic_prefix):
    print(f'Opening {main_file}...')

    # Getting text from file
    with open(main_file, 'r', encoding='utf-8') as file:
        data = file.read()

    print('Done')

    print('Processing file...')

    # Editting the file text
    data = process_file_data(base, data, subtopic_prefix)

    print('Done')

    print('Writing results...')
    # Writing the result
    write_result(main_file, data)

    print('Done')

    print(main_file, 'updated succesfully!')

def main():
    args = sys.argv
    subtopic_prefix = "    - "
    try:
        # -a stands for "all or auto"
        if '-a' in args:
            # Gets the current dir data, and gets the subdirs
            dirs = list(os.walk(os.getcwd()))[0][1]
            for directory in dirs:
                main_file = os.path.join(directory, 'README.md')
                if directory not in IGNORE_DIRS and os.path.exists(main_file):
                    add_subtopics(directory, main_file, subtopic_prefix)
            sys.exit(1)

        # Getting the base dir
        base = args[1].replace('\\', '')
        main_file = os.path.join(base, 'README.md')

        if args[-1] != base:
            subtopic_prefix = args[-1].replace('"', '')

        add_subtopics(base, main_file, subtopic_prefix)

    except IndexError:
        print(DOCSTRING)
        sys.exit(1)
    except FileNotFoundError:
        print(main_file, 'not found')
        sys.exit(1)


# -a stands for auto

if __name__ == "__main__":
    main()