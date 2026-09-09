import re

css_append = """
/* ---- Article Cover Image ---- */
.article-cover-img {
    width: 100%;
    max-width: 760px;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    border-radius: 16px;
    margin: 0 auto 40px;
    display: block;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}
"""

with open('blog/blog.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

images = {
    'blog/cara-atur-jadwal-posting-instagram-biar-konsisten.html': 'https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=1200&auto=format&fit=crop',
    'blog/cara-bikin-caption-jualan-yang-menarik-pembeli.html': 'https://images.unsplash.com/photo-1455390582262-044cdead2708?q=80&w=1200&auto=format&fit=crop',
    'blog/kapan-harus-pakai-agency-media-sosial.html': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop',
    'blog/kelola-sosmed-online-tanpa-ribet-untuk-umkm.html': 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?q=80&w=1200&auto=format&fit=crop',
    'blog/sosial-media-marketing-untuk-umkm-panduan-lengkap.html': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop'
}

for file_path, img_url in images.items():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if image already exists to avoid duplicates if run multiple times
    if 'class="article-cover-img"' not in content:
        img_tag = f'\n    <img src="{img_url}" alt="Cover Artikel" class="article-cover-img" loading="lazy">\n'
        
        # Insert after </header>
        content = re.sub(r'(</header>)', r'\1' + img_tag, content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Images and CSS added.")
