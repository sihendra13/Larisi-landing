import re
import glob

img_map = {
    'cara-atur-jadwal-posting-instagram-biar-konsisten': 'blog_schedule.jpg',
    'cara-bikin-caption-jualan-yang-menarik-pembeli': 'blog_caption.jpg',
    'kapan-harus-pakai-agency-media-sosial': 'blog_agency.jpg',
    'kelola-sosmed-online-tanpa-ribet-untuk-umkm': 'blog_umkm.jpg',
    'sosial-media-marketing-untuk-umkm-panduan-lengkap': 'blog_strategy.jpg'
}

for file in glob.glob('blog/*.html'):
    if file == 'blog/index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slug = file.replace('blog/', '').replace('.html', '')
    if slug in img_map:
        new_og_image = f'https://www.larisi.id/Assets/blog/{img_map[slug]}'
        
        # Replace the old og:image
        content = re.sub(
            r'<meta property="og:image" content="[^"]+">',
            f'<meta property="og:image" content="{new_og_image}">',
            content
        )
        
        # Also replace twitter:image if it exists
        content = re.sub(
            r'<meta name="twitter:image" content="[^"]+">',
            f'<meta name="twitter:image" content="{new_og_image}">',
            content
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("OG Images updated for all blog articles.")
