# Kebijakan keamanan dan data

**Status:** prototipe penelitian, belum production hardened.

- `.joblib` berbasis pickle dan **bisa menjalankan kode berbahaya** saat dimuat. Hanya gunakan model hasil Kaggle sendiri yang asal-usulnya diverifikasi; jangan izinkan user upload model secara acak.
- API telah membatasi target sesuai daftar, input `.csv`, 10 MiB, 2.000 baris, nama fitur dan nilai numerik finite. Tambahkan login, RBAC, rate limit dan audit sebelum dibuka ke publik.
- Jangan commit `.env`, token, `kaggle.json`, credentials, data pabrik sensitif, dataset mentah, file ZIP besar, cache. Bila token pernah ter-push, `.gitignore` tidak menghapus histori: segera rotasi kredensial.
- Jangan log semua isi CSV; klasifikasi apakah telemetry berisi informasi milik perusahaan dan tetapkan kebijakan penyimpanan/penghapusan serta izin penggunaan.
- Pastikan CORS terbatas, HTTPS, model checksum/signing, dependensi pinned dan scanning kerentanan. Saat deployment, data dan license dari UCI/NASA tetap punya ketentuan terpisah dari lisensi kode.
- Indikator IMS tidak boleh digunakan untuk pemutusan peralatan otomatis; diperlukan validasi dan keputusan manusia.

Pelaporan isu keamanan sebaiknya menggunakan komunikasi privat pemilik repository/GitHub private vulnerability reporting jika tersedia. Belum ada penetration test yang diklaim. Detail: [English security](../en/SECURITY.md).
