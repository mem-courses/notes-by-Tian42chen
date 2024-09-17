import os
import re
from os import path

dirname = path.abspath(path.dirname(__file__))

source_dir = path.join(dirname, "frame")
temp_dir = path.join(dirname, "tmp")
if not path.exists(temp_dir):
    os.makedirs(temp_dir)
output_dir = path.join(dirname, "target")
if not path.exists(output_dir):
    os.makedirs(output_dir)

source_files = [path.join(source_dir, file) for file in os.listdir(source_dir) if file.endswith(".tex")]

# preprocess the tex file


def preprocess_convert(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'\\textbf{(.*?)}', r' \\textbf{\1} ', content)
    content = re.sub(r'\\highlight{(.*?)}', r' \\textbf{\1} ', content)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


# use pandoc to convert tex to md
def pandoc_convert(source_file, output_file):
    os.system('pandoc -s -t markdown "{}" -o "{}"'.format(source_file, output_file))


source_files = source_files[:1]
for source_file in source_files:
    basename = path.basename(source_file)[:-4]
    temp_file = path.join(temp_dir, basename + '.tex')
    preprocess_convert(source_file, temp_file)
    output_file = path.join(output_dir, basename + '.md')
    pandoc_convert(temp_file, output_file)
