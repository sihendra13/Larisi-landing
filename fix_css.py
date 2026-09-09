import re

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .blog-card padding
css = css.replace(
    '.blog-card {\n    background: #FFFFFF;\n    padding: 32px 28px;',
    '.blog-card {\n    background: #FFFFFF;\n    padding: 0;\n    overflow: hidden;'
)

# Append new styles
if '.blog-card-img' not in css:
    css += """
.blog-card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-bottom: 1px solid #EBEBEB;
}
.blog-card-content {
    padding: 28px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}
"""
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# Update blog/blog.css
with open('blog/blog.css', 'r', encoding='utf-8') as f:
    bcss = f.read()

# Replace .blog-index-card padding
bcss = bcss.replace(
    '.blog-index-card {\n    display: block;\n    text-decoration: none;\n    border: 1px solid #eef0f5;\n    border-radius: 16px;\n    padding: 28px;',
    '.blog-index-card {\n    display: flex;\n    flex-direction: column;\n    text-decoration: none;\n    border: 1px solid #eef0f5;\n    border-radius: 16px;\n    padding: 0;\n    overflow: hidden;'
)
if '.blog-index-card-img' not in bcss:
    bcss += """
.blog-index-card-img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-bottom: 1px solid #eef0f5;
}
.blog-index-card-content {
    padding: 28px;
    flex-grow: 1;
}
"""

# Replace .related-card padding
bcss = bcss.replace(
    '.related-card {\n    display: block;\n    text-decoration: none;\n    border: 1px solid #eef0f5;\n    border-radius: 14px;\n    padding: 22px;',
    '.related-card {\n    display: flex;\n    flex-direction: column;\n    text-decoration: none;\n    border: 1px solid #eef0f5;\n    border-radius: 14px;\n    padding: 0;\n    overflow: hidden;'
)
if '.related-card-img' not in bcss:
    bcss += """
.related-card-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    border-bottom: 1px solid #eef0f5;
}
.related-card-content {
    padding: 22px;
    flex-grow: 1;
}
"""

with open('blog/blog.css', 'w', encoding='utf-8') as f:
    f.write(bcss)

print("CSS updated.")
