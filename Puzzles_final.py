import shutil
import os
import re

# ------My solution------

shutil.unpack_archive('D:\\Python\\work_on_files\\unzip_me_for_instructions.zip',
                      'D:\\Python\\work_on_files\\unzipped_puzzles', 'zip')

file_path = 'D:\\Python\\work_on_files\\unzipped_puzzles\\extracted_content'

for folder, sub_folder, files in os.walk(file_path):
    for file in files:
        with open(f'{folder}\\{file}', 'r') as content:
            text = content.read()
            pattern = r'(\d{3})-(\d{3})-(\d{4})'
            number = re.search(pattern, text)
            if isinstance(number, re.Match):
                print(number.group())


# ------ Solution based on the course ------


results = []


def search(file, pattern = r'(\d{3})-(\d{3})-(\d{4})'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


for folder, sub_folder, files in os.walk(os.getcwd()):

    for file in files:
        full_path = folder+'\\'+file
        if search(full_path) != '':
            results.append(search(full_path).group())
print(results)
