import re
import glob

# 1. Update CSS
css_append = """
/* ---- Article Share Buttons ---- */
.article-share {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 28px 0;
    border-top: 1px solid #eef0f5;
    border-bottom: 1px solid #eef0f5;
    padding: 16px 0;
}

.share-label {
    font-size: 14px;
    font-weight: 700;
    color: var(--gray-text);
    margin-right: 4px;
}

.share-btn {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f1f3f7;
    color: #64748b;
    transition: all 0.2s;
    border: none;
    cursor: pointer;
    text-decoration: none;
}

.share-btn svg {
    width: 18px;
    height: 18px;
    fill: currentColor;
}

/* Hover Colors */
.share-btn:hover.wa { background: #25D366; color: #fff; }
.share-btn:hover.fb { background: #1877F2; color: #fff; }
.share-btn:hover.in { background: #0A66C2; color: #fff; }
.share-btn:hover.th { background: #000000; color: #fff; }
.share-btn:hover.copy { background: var(--primary); color: #fff; }

.copy-toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%) translateY(100px);
    background: #1f2937;
    color: white;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 14px;
    font-weight: 500;
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    z-index: 1000;
    pointer-events: none;
}

.copy-toast.show {
    transform: translateX(-50%) translateY(0);
    opacity: 1;
}
"""

with open('blog/blog.css', 'r', encoding='utf-8') as f:
    if '.article-share' not in f.read():
        with open('blog/blog.css', 'a', encoding='utf-8') as fa:
            fa.write(css_append)

# 2. HTML to Inject
def get_share_html(slug, encoded_title):
    url = f"https://www.larisi.id/blog/{slug}.html"
    
    # SVG Paths
    wa_svg = '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
    fb_svg = '<path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>'
    in_svg = '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>'
    th_svg = '<path d="M14.938 12.008c0 .285-.018.575-.052.868-.694.025-1.428.026-2.222.026-.814 0-1.558-.002-2.268-.028-.035-.292-.054-.582-.054-.866 0-.301.02-.6.054-.897.68-.027 1.422-.03 2.215-.03.784 0 1.542.004 2.247.03.036.294.054.59.054.897m-2.126-3.238c-.37-.02-.82-.032-1.32-.032-.485 0-.916.01-1.284.03-.43.493-.728 1.18-.813 1.986.726.027 1.465.03 2.238.03.754 0 1.472-.003 2.19-.028-.088-.8-.382-1.488-.81-1.983L12.812 8.77zm4.33-1.077c-.503-.984-1.21-1.83-2.128-2.434-.847-.565-1.884-.882-3.14-.882-1.246 0-2.3.33-3.084.877-.92.64-1.638 1.492-2.133 2.476-.563 1.12-1.004 2.766-1.004 4.195 0 1.442.443 3.14 1.012 4.282.5 1 1.215 1.854 2.138 2.493.85.592 1.83.89 3.03.89 1.157 0 2.24-.26 3.064-.78.473-.3.94-.746 1.343-1.233.1-.122.096-.282.017-.4-.067-.102-.152-.162-.257-.183-.43-.08-1.576-.328-2.222-.444-.132-.023-.277.013-.377.108-.074.07-.123.143-.162.2-.18.25-.436.568-.707.755-.38.26-1.144.333-1.597.333-.95 0-1.815-.224-2.483-.69-.942-.656-1.592-1.728-1.93-2.887.89-.04 1.95-.047 3.193-.047 1.24 0 2.302.007 3.19.047.387-1.126 1.054-2.213 1.998-2.89.81-.585 1.706-.856 2.65-.856.786 0 1.455.19 2.01.52.553.33.91.758 1.117 1.324.232.637.208 1.41.21 2.224v1.314c0 1.428-.482 2.733-1.265 3.513-.778.775-1.986 1.14-3.642 1.14h-1.63c-2.3 0-4.048-1.107-5.074-2.894-.962-1.678-1.42-3.882-1.42-5.757 0-1.87.458-4.053 1.425-5.733 1.01-1.75 2.723-2.822 4.966-2.822 2.25 0 3.978 1.077 4.986 2.826 1.026 1.773 1.487 3.996 1.487 5.753v1.35c0 1.06.1 1.637.49 2.025.378.375 1.134.625 2.122.625.6 0 1.355-.102 2.062-.395a12.016 12.016 0 005.105-4.225 11.968 11.968 0 002.327-7.24c0-6.626-5.373-12-12-12s-12 5.374-12 12c0 6.628 5.373 12 12 12a11.91 11.91 0 008.243-3.324.5.5 0 10-.707-.707A10.912 10.912 0 0112 23c-6.075 0-11-4.925-11-11 0-6.074 4.925-11 11-11 6.076 0 11 4.926 11 11 0 2.247-.69 4.34-1.858 6.096a11.028 11.028 0 01-4.634 3.865c-.775.318-1.633.433-2.285.433-1.282 0-2.316-.36-3.003-1.042-.683-.68-.992-1.73-.992-3.136v-1.352c0-1.736-.45-3.876-1.423-5.56m1.096 4.945c-1.356 0-2.583-.005-3.607-.037.19 1.162.776 2.115 1.572 2.67.575.402 1.3.604 2.13.604.815 0 1.536-.188 2.056-.554.786-.55 1.34-1.528 1.536-2.73-1.077.034-2.326.047-3.687.047M12 24C5.373 24 0 18.627 0 12S5.373 0 12 0s12 5.373 12 12-5.373 12-12 12z"/>'
    copy_svg = '<path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>'
    
    html = f"""
        <div class="article-share">
            <span class="share-label">Bagikan:</span>
            <a href="https://api.whatsapp.com/send?text={encoded_title}%20-%20{url}" target="_blank" class="share-btn wa" title="Bagikan ke WhatsApp">
                <svg viewBox="0 0 24 24">{wa_svg}</svg>
            </a>
            <a href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" class="share-btn fb" title="Bagikan ke Facebook">
                <svg viewBox="0 0 24 24">{fb_svg}</svg>
            </a>
            <a href="https://www.threads.net/intent/post?text={encoded_title}%20-%20{url}" target="_blank" class="share-btn th" title="Bagikan ke Threads">
                <svg viewBox="0 0 24 24">{th_svg}</svg>
            </a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" class="share-btn in" title="Bagikan ke LinkedIn">
                <svg viewBox="0 0 24 24">{in_svg}</svg>
            </a>
            <button onclick="copyArticleLink('{url}')" class="share-btn copy" title="Salin Tautan">
                <svg viewBox="0 0 24 24">{copy_svg}</svg>
            </button>
        </div>
"""
    return html

# 3. Add to HTML files
blog_files = glob.glob('blog/*.html')

script_js = """
<script>
function copyArticleLink(url) {
    navigator.clipboard.writeText(url).then(() => {
        let toast = document.getElementById('copyToast');
        if(!toast) {
            toast = document.createElement('div');
            toast.id = 'copyToast';
            toast.className = 'copy-toast';
            toast.textContent = 'Tautan berhasil disalin!';
            document.body.appendChild(toast);
        }
        
        // trigger reflow
        void toast.offsetWidth;
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    });
}
</script>
"""

import urllib.parse

for file_path in blog_files:
    if file_path == 'blog/index.html': continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    slug = file_path.replace('blog/', '').replace('.html', '')
    
    # Extract Title for encoding
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else "Artikel Larisi"
    encoded_title = urllib.parse.quote(title)
    
    share_block = get_share_html(slug, encoded_title)
    
    # Insert AFTER <div class="article-meta">...</div>
    if '<div class="article-share">' not in content:
        content = re.sub(r'(<div class="article-meta">.*?</div>)', r'\1' + share_block, content, flags=re.DOTALL)
        
        # Insert BEFORE <section class="related-section"> for the bottom one
        # Actually better: At the end of <article class="article-body">
        content = content.replace('</article>', share_block + '\n    </article>')
        
        # Add JS script before </body>
        if 'function copyArticleLink' not in content:
            content = content.replace('</body>', script_js + '\n</body>')
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Share buttons and Threads added.")
