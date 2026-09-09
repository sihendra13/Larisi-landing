import re
import glob

# Mapping URLs
img_map = {
    'cara-atur-jadwal-posting-instagram-biar-konsisten': '/Assets/blog/blog_schedule.jpg',
    'cara-bikin-caption-jualan-yang-menarik-pembeli': '/Assets/blog/blog_caption.jpg',
    'kapan-harus-pakai-agency-media-sosial': '/Assets/blog/blog_agency.jpg',
    'kelola-sosmed-online-tanpa-ribet-untuk-umkm': '/Assets/blog/blog_umkm.jpg',
    'sosial-media-marketing-untuk-umkm-panduan-lengkap': '/Assets/blog/blog_strategy.jpg'
}

# 1. Fix broken images inside detail pages
blog_files = glob.glob('blog/*.html')
for file_path in blog_files:
    if file_path == 'blog/index.html': continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace any unsplash URL with the local one
    slug = file_path.replace('blog/', '').replace('.html', '')
    if slug in img_map:
        content = re.sub(r'<img src="https://images.unsplash.com[^"]+"', f'<img src="{img_map[slug]}"', content)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Detail images fixed.")
