import re

css_append = """
/* ===== TESTIMONIAL SECTION ===== */
.testimonial-section {
    padding: 100px 8% 80px;
    background: #FFFFFF;
    text-align: center;
    max-width: 100%;
}

.testimonial-header {
    margin-bottom: 56px;
}

.testimonial-header .section-tag {
    color: var(--primary);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.testimonial-header h2 {
    font-size: 40px;
    font-weight: 900;
    color: var(--dark);
    margin-top: 16px;
    line-height: 1.2;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 32px;
    max-width: 1200px;
    margin: 0 auto;
}

.testimonial-card {
    background: #FFFFFF;
    border: 1px solid #eef0f5;
    border-radius: 16px;
    padding: 40px 32px;
    text-align: left;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.03);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.testimonial-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
    border-color: var(--primary);
}

.testimonial-stars {
    color: #FFB800;
    font-size: 20px;
    margin-bottom: 20px;
}

.testimonial-text {
    font-size: 16px;
    color: #4b5563;
    line-height: 1.7;
    margin-bottom: 32px;
    font-style: italic;
}

.testimonial-author {
    display: flex;
    align-items: center;
    gap: 16px;
}

.author-avatar {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: var(--primary);
    color: #FFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    font-size: 22px;
}

.author-info h4 {
    font-size: 16px;
    font-weight: 700;
    color: var(--dark);
    margin-bottom: 4px;
}

.author-info p {
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 4px;
}

.author-info a {
    font-size: 14px;
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
}

.author-info a:hover {
    text-decoration: underline;
}

@media (max-width: 768px) {
    .testimonial-section {
        padding: 60px 5% 60px;
    }
    .testimonial-header h2 {
        font-size: 28px;
    }
    .testimonial-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.testimonial-section' not in css:
    with open('style.css', 'a', encoding='utf-8') as fa:
        fa.write(css_append)

html_section = """
    <!-- ===== TESTIMONIAL SECTION ===== -->
    <section class="testimonial-section" id="testimoni">
        <div class="testimonial-header">
            <span class="section-tag">APA KATA MEREKA</span>
            <h2>Lebih dari 500+ UMKM terbantu oleh Larisi</h2>
        </div>
        <div class="testimonial-grid">
            <!-- Card 1 -->
            <div class="testimonial-card">
                <div class="testimonial-stars">⭐⭐⭐⭐⭐</div>
                <p class="testimonial-text">"Dulu tiap malam harus begadang cuma buat posting jualan. Sejak pakai Larisi, saya tinggal jadwalkan konten sebulan penuh tiap hari Minggu. Sekarang saya bisa lebih fokus urus produksi dan keluarga."</p>
                <div class="testimonial-author">
                    <div class="author-avatar">B</div>
                    <div class="author-info">
                        <h4>Budi S.</h4>
                        <p>Pemilik Usaha Kuliner</p>
                        <a href="https://instagram.com/" target="_blank">@kedai.budis</a>
                    </div>
                </div>
            </div>
            
            <!-- Card 2 -->
            <div class="testimonial-card">
                <div class="testimonial-stars">⭐⭐⭐⭐⭐</div>
                <p class="testimonial-text">"Gak perlu lagi pusing bolak-balik buka aplikasi Instagram, Facebook, dan TikTok satu per satu. Lewat Larisi, saya pantau semua interaksi pelanggan dari satu layar. Kerjaan admin 3x lebih cepat!"</p>
                <div class="testimonial-author">
                    <div class="author-avatar" style="background:#10b981;">S</div>
                    <div class="author-info">
                        <h4>Sari Amalia</h4>
                        <p>Owner Fashion Muslim</p>
                        <a href="https://instagram.com/" target="_blank">@sari.hijabku</a>
                    </div>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="testimonial-card">
                <div class="testimonial-stars">⭐⭐⭐⭐⭐</div>
                <p class="testimonial-text">"Aplikasi paling pas untuk UMKM yang baru merintis. Awalnya kepikiran mau sewa jasa admin sosmed yang mahal, ternyata pakai Larisi semua dikelola sendiri dengan rapi. Sangat worth it."</p>
                <div class="testimonial-author">
                    <div class="author-avatar" style="background:#f59e0b;">A</div>
                    <div class="author-info">
                        <h4>Anton Wibowo</h4>
                        <p>Distributor Kosmetik</p>
                        <a href="https://instagram.com/" target="_blank">@anton.skincare</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="testimoni"' not in html:
    # Insert right before the PRICING SECTION
    html = html.replace('<!-- ===== PRICING SECTION ===== -->', html_section + '    <!-- ===== PRICING SECTION ===== -->')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Testimonial section added.")
