from bs4 import BeautifulSoup, Doctype
import os

def convert_html(input_file):
    # Read the old HTML content from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        old_html = file.read()

    soup = BeautifulSoup(old_html, 'html.parser')
    
    # Update doctype
    if len(soup.contents) > 0 and isinstance(soup.contents[0], Doctype):
        soup.contents[0].replace_with(Doctype('html'))
    else:
        soup.insert(0, Doctype('html'))
    
    # Set charset meta tag
    if not soup.find('meta', charset=True):
        meta_charset = soup.new_tag('meta', charset='UTF-8')
        soup.head.insert(0, meta_charset)

    # Update tags to HTML5 semantic elements
    tag_mapping = {
        'b': 'strong',
        'i': 'em',
        'u': 'ins',
        'center': 'div',
        'font': 'span'
    }
    for old_tag, new_tag in tag_mapping.items():
        for tag in soup.find_all(old_tag):
            tag.name = new_tag
    
    # Remove deprecated attributes
    deprecated_attrs = ['bgcolor', 'border', 'cellpadding', 'cellspacing', 'align', 'valign']
    for tag in soup.find_all(True):
        for attr in deprecated_attrs:
            if attr in tag.attrs:
                del tag.attrs[attr]

    # Add basic responsive viewport meta tag
    if not soup.find('meta', {'name': 'viewport'}):
        meta_viewport = soup.new_tag('meta', content='width=device-width, initial-scale=1.0')
        meta_viewport.name = 'viewport'
        soup.head.append(meta_viewport)

    # Write the modified HTML to the output file
    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            yield file_path

# Example usage
directory = 'book'  # Replace '/path/to/your/directory' with the path to your directory
for file_path in list_files(directory):
    if file_path.endswith('.htm') or file_path.endswith('.html'):
        try:
            convert_html(file_path)
        except:
            print(file_path)