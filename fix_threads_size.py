import re
import glob

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change 24px to 18px
    content = content.replace('style="width: 24px; height: 24px; border-radius: 50%;"', 'style="width: 18px; height: 18px; border-radius: 50%;"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Threads image resized to 18px.")
