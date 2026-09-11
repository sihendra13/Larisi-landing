import re
import glob

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Append .html to og:url
    content = re.sub(
        r'<meta property="og:url" content="(https://www\.larisi\.id/blog/[^"]+)(?<!\.html)">',
        r'<meta property="og:url" content="\1.html">',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed og:url tags.")
