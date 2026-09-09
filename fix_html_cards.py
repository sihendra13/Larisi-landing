import re
import glob

img_map = {
    'cara-atur-jadwal-posting-instagram-biar-konsisten': '/Assets/blog/blog_schedule.jpg',
    'cara-bikin-caption-jualan-yang-menarik-pembeli': '/Assets/blog/blog_caption.jpg',
    'kapan-harus-pakai-agency-media-sosial': '/Assets/blog/blog_agency.jpg',
    'kelola-sosmed-online-tanpa-ribet-untuk-umkm': '/Assets/blog/blog_umkm.jpg',
    'sosial-media-marketing-untuk-umkm-panduan-lengkap': '/Assets/blog/blog_strategy.jpg'
}

def get_slug(url):
    m = re.search(r'/blog/([^".]+)', url)
    if m: return m.group(1)
    return None

# 1. Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_index_card(match):
    full = match.group(0)
    if '<div class="blog-card-content">' in full: return full # Already processed
    url = match.group(1)
    slug = get_slug(url)
    if not slug or slug not in img_map: return full
    img_src = img_map[slug]
    
    # Extract inner content
    inner = match.group(2)
    return f'<a href="{url}" class="blog-card">\n                <img src="{img_src}" alt="Cover" class="blog-card-img" loading="lazy">\n                <div class="blog-card-content">\n{inner}\n                </div>\n            </a>'

content = re.sub(r'<a href="([^"]+)" class="blog-card">(.*?)</a>', replace_index_card, content, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Fix blog/index.html
with open('blog/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_blog_index_card(match):
    full = match.group(0)
    if '<div class="blog-index-card-content">' in full: return full
    url = match.group(1)
    slug = get_slug(url)
    if not slug or slug not in img_map: return full
    img_src = img_map[slug]
    
    inner = match.group(2)
    return f'<a href="{url}" class="blog-index-card">\n                <img src="{img_src}" alt="Cover" class="blog-index-card-img" loading="lazy">\n                <div class="blog-index-card-content">\n{inner}\n                </div>\n            </a>'

content = re.sub(r'<a href="([^"]+)" class="blog-index-card">(.*?)</a>', replace_blog_index_card, content, flags=re.DOTALL)
with open('blog/index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 3. Fix related cards in all blog/*.html
blog_files = glob.glob('blog/*.html')
for file_path in blog_files:
    if file_path == 'blog/index.html': continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def replace_related_card(match):
        full = match.group(0)
        if '<div class="related-card-content">' in full: return full
        url = match.group(1)
        slug = get_slug(url)
        if not slug or slug not in img_map: return full
        img_src = img_map[slug]
        
        inner = match.group(2)
        return f'<a href="{url}" class="related-card">\n                <img src="{img_src}" alt="Cover" class="related-card-img" loading="lazy">\n                <div class="related-card-content">\n{inner}\n                </div>\n            </a>'

    content = re.sub(r'<a href="([^"]+)" class="related-card">(.*?)</a>', replace_related_card, content, flags=re.DOTALL)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML Cards updated.")
