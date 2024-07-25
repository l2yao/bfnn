from bs4 import BeautifulSoup
import os

def strip_font_tags(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all <font> tags
    font_tags = soup.find_all('font')
    
    # Replace each <font> tag with its contents
    for tag in font_tags:
        tag.unwrap()
    
    # Return the modified HTML
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
        strip_font_tags(file_path)