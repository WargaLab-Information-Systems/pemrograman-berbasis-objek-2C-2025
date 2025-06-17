<?php
function kutipanMotivasi() {
    $quotes = [
        "Jangan menyerah, semua hal besar butuh waktu.",
        "Kegagalan adalah guru terbaik.",
        "Percaya diri adalah kunci.",
        "Belajar adalah investasi jangka panjang."
    ];
    return $quotes[array_rand($quotes)];
}

$artikel = [
    1 => [
        'judul' => 'Belajar PHP',
        'tanggal' => '2025-04-01',
        'refleksi' => 'Mempelajari dasar-dasar PHP membuat saya lebih paham logika backend.',
        'gambar' => 'php.png',
        'referensi' => 'https://www.php.net'
    ],
    2 => [
        'judul' => 'Belajar Dasar HTML & CSS',
        'tanggal' => '2025-04-20',
        'refleksi' => 'Menguasai dasar HTML dan CSS membuka pintu untuk membangun website yang menarik.',
        'gambar' => 'html.png',
        'referensi' => null
    ],
];

$id = $_GET['id'] ?? null;
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Blog Reflektif</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container py-4">
    <nav class="nav mb-4">
        <a class="nav-link" href="profil_interaktif.php">Profil</a>
        <a class="nav-link" href="timeline_pengalaman.php">Timeline</a>
        <a class="nav-link active" href="blog.php">Blog</a>
    </nav>

    <?php if ($id && isset($artikel[$id])): ?>
        <div class="card">
            <img src="<?= $artikel[$id]['gambar'] ?>" class="img-fluid" alt="gambar" style="max-width: 400px; height: auto; float: left; margin-right: 15px; margin-bottom: 10px;">
            <div class="card-body">
                <h3 class="card-title"><?= $artikel[$id]['judul'] ?></h3>
                <h6 class="text-muted"><?= $artikel[$id]['tanggal'] ?></h6>
                <p><?= $artikel[$id]['refleksi'] ?></p>
                <blockquote class="blockquote"><?= kutipanMotivasi() ?></blockquote>
                <?php if ($artikel[$id]['referensi']): ?>
                    <p>Referensi: <a href="<?= $artikel[$id]['referensi'] ?>" target="_blank"><?= $artikel[$id]['referensi'] ?></a></p>
                <?php endif; ?>
                <a href="blog.php" class="btn btn-outline-primary">← Kembali</a>
            </div>
        </div>
    <?php else: ?>
        <h2>Daftar Artikel</h2>
        <ul class="list-group">
            <?php foreach ($artikel as $key => $data): ?>
                <li class="list-group-item d-flex justify-content-between">
                    <span><strong><?= $data['judul'] ?></strong><br><small><?= $data['tanggal'] ?></small></span>
                    <a href="?id=<?= $key ?>" class="btn btn-sm btn-primary">Baca</a>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
</div>
</body>
</html>
