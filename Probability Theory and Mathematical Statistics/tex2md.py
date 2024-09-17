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


def preprocess(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'\, ', '，', content)
    content = re.sub(r'\. ', '。', content)
    content = re.sub(r'\: ', '：', content)
    content = re.sub(r'\; ', '；', content)
    content = re.sub(r'\.\n', '。\n', content)
    content = re.sub(r'\$', r' $ ', content)
    content = re.sub(r'\\textbf{(.*?)}', r' \\textbf{\1} ', content)
    content = re.sub(r'\\highlight{(.*?)}', r' \\textbf{\1} ', content)
    content = re.sub(r'\\begin{align\*}\s+', r'\\begin{align*}', content)
    content = re.sub(r'\s+\\end{align\*}', r'\\end{align*}', content)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


def postprocess(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<div class="definition">\n+', '<span class="m-definition"></span> ', content)
    content = re.sub(r'<div class="theorem">\n+', '<span class="m-theorem"></span> ', content)
    content = re.sub(r'</div>', '', content)
    content = re.sub(r'\x20*，\x20*', '，', content)
    content = re.sub(r'\x20*。\x20*', '。', content)
    content = re.sub(r'\x20*；\x20*', '；', content)
    content = re.sub(r'\x20*：\x20*', '：', content)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)


# use pandoc to convert tex to md
def pandoc_convert(source_file, output_file):
    os.system('pandoc --wrap=none -s -t gfm "{}" -o "{}"'.format(source_file, output_file))


for source_file in source_files:
    basename = path.basename(source_file)[:-4]
    temp_tex_file = path.join(temp_dir, basename + '.tex')
    temp_md_file = path.join(temp_dir, basename + '.md')
    output_file = path.join(output_dir, basename + '.md')
    preprocess(source_file, temp_tex_file)
    pandoc_convert(temp_tex_file, temp_md_file)
    postprocess(temp_md_file, output_file)
