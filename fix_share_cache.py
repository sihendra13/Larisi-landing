import re
import glob

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Facebook: add ?v=2 to the u= parameter
    content = re.sub(
        r'sharer\.php\?u=(https://www\.larisi\.id/blog/[^"]+\.html)',
        r'sharer.php?u=\1?v=2',
        content
    )
    
    # WhatsApp: text parameter
    content = re.sub(
        r'whatsapp://send\?text=([^"]+)%20-%20(https://www\.larisi\.id/blog/[^"]+\.html)',
        r'whatsapp://send?text=\1%20-%20\2?v=2',
        content
    )
    
    # LinkedIn: url parameter
    content = re.sub(
        r'linkedin\.com/sharing/share-offsite/\?url=(https://www\.larisi\.id/blog/[^"]+\.html)',
        r'linkedin.com/sharing/share-offsite/?url=\1?v=2',
        content
    )
    
    # Threads: text parameter
    content = re.sub(
        r'threads\.net/intent/post\?text=([^"]+)%20-%20(https://www\.larisi\.id/blog/[^"]+\.html)',
        r'threads.net/intent/post?text=\1%20-%20\2?v=2',
        content
    )

    # Note: Copy Link button uses JS window.location.href, we can leave that alone because it's just copying.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added ?v=2 to all share links.")
