import glob

# Find all HTML files
html_files = glob.glob('/home/kevin/Downloads/coexistence-walk_webseite/*.html')

target = '<li><a href="https://www.coexistence-walk.de" target="_blank">www.coexistence-walk.de</a></li>'
replacement = '''<li><a href="https://www.coexistence-walk.de" target="_blank">www.coexistence-walk.de</a></li>
            <li><a href="https://www.facebook.com/coexistencewalk/" target="_blank" rel="noopener noreferrer">Facebook: coexistencewalk</a></li>'''

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content and "Facebook: coexistencewalk" not in content:
        content = content.replace(target, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

