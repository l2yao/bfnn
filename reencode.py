from bs4 import BeautifulSoup
import os
import codecs

def convert_html_from_big5_to_utf8(html_file):
    with codecs.open(html_file, 'r', 'big5', errors='ignore') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    utf8_html = soup.prettify(encoding='utf-8')

    with open(html_file, 'wb') as f:
        f.write(utf8_html)

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path

# Example usage:
directory = 'book'  # Replace '/path/to/your/directory' with the path to your directory
for file_path in list_files(directory):
    if file_path.endswith('.htm') or file_path.endswith('.html'):
        convert_html_from_big5_to_utf8(file_path)