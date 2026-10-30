# FAQ — Pertanyaan umum

**Apa MachineAnomaly?** Proyek riset full-stack untuk klasifikasi kondisi komponen Hydraulic dan indikator perubahan getaran IMS, bukan prediktor kerusakan mesin tersertifikasi.

**Apakah kedua dataset digabung training?** Tidak. UCI punya label kondisi, IMS tidak punya label per-snapshot. Model, evaluasi dan skalanya terpisah.

**Kenapa macro-F1 hampir 100%?** Experiment 02 memakai split stratified acak pada dataset yang sama; hasilnya valid untuk protokol itu saja, bukan otomatis valid di pabrik lain. Experiment 01 kronologis punya hasil yang lebih buruk pada beberapa target.

**Apa hasil cooler 100 class 3 berarti error?** Tidak otomatis: 100 baris awal UCI memang memiliki label cooler class 3. Uji kelas lain untuk verifikasi.

**Apa 7/7 berarti semua sudah dites?** Tidak. Artinya 7 file path model ditemukan; sampai bukti yang ada, UI cooler 100 baris telah berhasil.

**Berapa maksimum CSV?** 2.000 baris, 10 MiB per request. Full CSV 2.205 baris perlu dibagi. Auto-batching belum diimplementasikan.

**Apa IMS alarm berarti bearing rusak?** Tidak. Itu indikator deviasi dari skor referensi awal, tanpa label fault waktu yang tervalidasi.

**Confidence proxy 0,9 berarti 90% kemungkinan gagal?** Tidak. Output tree ensemble bukan probabilitas kerusakan yang dikalibrasi.

**Kenapa frontend tidak menerima data PS1.txt langsung?** Model menggunakan fitur hasil preprocessing. API belum mempunyai layanan raw-signal-to-feature.

**Haruskah model dan dataset masuk GitHub?** Dataset mentah jangan. Model joblib hanya jika sumbernya tepercaya, lisensi/ukuran tepat, dan aman; repo kode tidak otomatis melegalkan redistribusi dataset.

**Proyek sudah final?** Selesai untuk milestone notebook Day 25 dan demo lokal, tetapi belum untuk deployment publik dan evaluasi hardware nyata.

**Di mana sumber bukti?** Notebook `notebooks/`, `reports/`, grafik `assets/plots/`, [metodologi](RESEARCH.md), [testing](TESTING.md).
