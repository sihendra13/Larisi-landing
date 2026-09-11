with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add .html to all blog article links that don't have it
import re
content = re.sub(
    r'href="(/blog/[a-z0-9\-]+)"(?!\s*class="blog-index-card">)',
    lambda m: m.group(0),
    content
)

# More targeted: fix only the blog-index-card links
content = re.sub(
    r'href="(/blog/[a-z0-9\-]+)" class="blog-index-card"',
    lambda m: f'href="{m.group(1)}.html" class="blog-index-card"',
    content
)

with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed blog/index.html links")
