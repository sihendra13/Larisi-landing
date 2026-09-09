import re
import glob

# Safe, simple X (Twitter) SVG
x_svg = '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Threads button entirely with X (Twitter)
    def replacer(match):
        url = match.group(1)
        encoded_title = match.group(2)
        # return X link
        return f'<a href="https://twitter.com/intent/tweet?url={url}&text={encoded_title}" target="_blank" class="share-btn th" title="Bagikan ke X (Twitter)">\n                {x_svg}\n            </a>'
    
    # We match the entire <a> tag for threads
    content = re.sub(
        r'<a href="https://www.threads.net/intent/post\?text=(.*?)%20-%20(.*?)" target="_blank" class="share-btn th" title="Bagikan ke Threads">\s*<svg.*?</svg>\s*</a>',
        replacer, 
        content, 
        flags=re.DOTALL
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Update hover color in CSS to black for X
with open('blog/blog.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Already .share-btn:hover.th { background: #000000; color: #fff; } which is perfect for X!

print("Replaced with X (Twitter) for stability.")
