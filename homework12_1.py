import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    text_without_tags = re.sub(r'<[^>]+>', '', html)
    cleaned_lines = [line.strip() for line in text_without_tags.splitlines()]
    cleaned_text = '\n'.join(line for line in cleaned_lines if line)

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write(cleaned_text)
pass