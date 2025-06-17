<?php
function buatItem($tahun, $judul, $deskripsi) {
    return "<div class='card mb-3'>
        <div class='card-header bg-primary text-white'>$tahun - $judul</div>
        <div class='card-body'><p class='card-text'>$desc</p></div>
    </div>";
}

$pengalaman = [
    ["tahun" => "2024", "judul" => "Masuk Universitas Trunojoyo Madura", "deskripsi" => "Memulai perjalanan sebagai mahasiswa di UTM jurusan Sistem Informasi."],
    ["tahun" => "2025 (Semester 2)", "judul" => "Belajar HTML, CSS, & Python", "deskripsi" => "Mulai belajar dasar-dasar pemrograman front-end dan back-end."],
    ["tahun" => "Semester 3", "judul" => "Coming Soon", "deskripsi" => "Petualangan berikutnya akan segera dimulai..."],
];
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Timeline Pengalaman Kuliah</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container py-4">
    <nav class="nav mb-4">
        <a class="nav-link" href="profil_interaktif.php">Profil</a>
        <a class="nav-link active" href="timeline_pengalaman.php">Timeline</a>
        <a class="nav-link" href="blog.php">Blog</a>
    </nav>

    <h2 class="mb-4">Timeline Pengalaman Kuliah</h2>
    <?php foreach ($pengalaman as $item): ?>
        <?= buatItem($item['tahun'], $item['judul'], $item['deskripsi']) ?>
    <?php endforeach; ?>
</div>
</body>
</html>
