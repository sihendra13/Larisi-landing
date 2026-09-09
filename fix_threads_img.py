import re
import glob

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the SVG inside the Threads link with an <img> tag pointing to the user's uploaded image
    def replacer(match):
        return match.group(1) + '<img src="/Assets/blog/threads.png" alt="Threads" style="width: 24px; height: 24px; border-radius: 50%;">'
    
    content = re.sub(
        r'(class="share-btn th" title="Bagikan ke Threads">\s*)<svg.*?</svg>', 
        replacer, 
        content, 
        flags=re.DOTALL
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Threads logo replaced with user's uploaded image.")
