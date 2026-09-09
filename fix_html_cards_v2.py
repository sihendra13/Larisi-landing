import re

img_map = {
    'cara-atur-jadwal-posting-instagram-biar-konsisten': '/Assets/blog/blog_schedule.jpg',
    'cara-bikin-caption-jualan-yang-menarik-pembeli': '/Assets/blog/blog_caption.jpg',
    'kapan-harus-pakai-agency-media-sosial': '/Assets/blog/blog_agency.jpg',
    'kelola-sosmed-online-tanpa-ribet-untuk-umkm': '/Assets/blog/blog_umkm.jpg',
    'sosial-media-marketing-untuk-umkm-panduan-lengkap': '/Assets/blog/blog_strategy.jpg'
}

def get_slug(url):
    # url is like "blog/..." or "/blog/..."
    # remove leading slash if present
    if url.startswith('/'): url = url[1:]
    m = re.search(r'blog/([^".]+)', url)
    if m: return m.group(1)
    return None

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_index_card(match):
    full = match.group(0)
    if '<div class="blog-card-content">' in full: return full # Already processed
    url = match.group(1)
    slug = get_slug(url)
    if not slug or slug not in img_map: return full
    img_src = img_map[slug]
    
    inner = match.group(2)
    return f'<a href="{url}" class="blog-card">\n                <img src="{img_src}" alt="Cover" class="blog-card-img" loading="lazy">\n                <div class="blog-card-content">\n{inner}\n                </div>\n            </a>'

content = re.sub(r'<a href="([^"]+)" class="blog-card">(.*?)</a>', replace_index_card, content, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed index.html")
