<?php
function tampilkanData($label, $value) {
    return "<tr><th>$label</th><td>$value</td></tr>";
}
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Profil Interaktif Mahasiswa</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container py-4">
    <nav class="nav mb-4">
        <a class="nav-link" href="profil_interaktif.php">Profil</a>
        <a class="nav-link" href="timeline_pengalaman.php">Timeline</a>
        <a class="nav-link" href="blog.php">Blog</a>
    </nav>

    <h1>Profil Interaktif Mahasiswa</h1>
    <form method="POST">
        <table class="table">
            <?= tampilkanData("Nama", "Adytta Putra Tarigan") ?>
            <?= tampilkanData("NIM", "240441100139") ?>
            <?= tampilkanData("Tempat, Tanggal Lahir", "Jakarta, 4 November 2005") ?>
            <?= tampilkanData("Email", "tariganadytta@gmail.com.com") ?>
            <?= tampilkanData("Nomor HP", "081384103822") ?>
        </table>

        <div class="mb-3">
            <label>Bahasa Pemrograman yang Dikuasai</label>
            <input type="text" name="bahasa[]" class="form-control mb-1">
            <input type="text" name="bahasa[]" class="form-control mb-1">
            <input type="text" name="bahasa[]" class="form-control">
        </div>

        <div class="mb-3">
            <label>Pengalaman Proyek</label>
            <textarea name="pengalaman" class="form-control"></textarea>
        </div>

        <div class="mb-3">
            <label>Software yang Sering Digunakan</label><br>
            <?php
            $softwareList = ['VS Code', 'XAMPP', 'Git'];
            foreach ($softwareList as $sw) {
                echo "<div class='form-check form-check-inline'>
                        <input class='form-check-input' type='checkbox' name='software[]' value='$sw'>
                        <label class='form-check-label'>$sw</label>
                      </div>";
            }
            ?>
        </div>

        <div class="mb-3">
            <label>Sistem Operasi</label><br>
            <?php
            foreach (['Windows', 'Linux', 'Mac'] as $os) {
                echo "<div class='form-check form-check-inline'>
                        <input class='form-check-input' type='radio' name='os' value='$os'>
                        <label class='form-check-label'>$os</label>
                      </div>";
            }
            ?>
        </div>

        <div class="mb-3">
            <label>Tingkat Penguasaan PHP</label>
            <select name="tingkat" class="form-select">
                <option value="Pemula">Pemula</option>
                <option value="Menengah">Menengah</option>
                <option value="Mahir">Mahir</option>
            </select>
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (!empty($_POST['bahasa'][0]) && !empty($_POST['pengalaman']) && !empty($_POST['software']) && !empty($_POST['os']) && !empty($_POST['tingkat'])) {
            $bahasa = array_filter($_POST['bahasa']);
            echo "<h4 class='mt-4'>Hasil Input:</h4><table class='table'>";
            echo tampilkanData("Bahasa Pemrograman", implode(', ', $bahasa));
            echo tampilkanData("Pengalaman Proyek", $_POST['pengalaman']);
            echo tampilkanData("Software", implode(', ', $_POST['software']));
            echo tampilkanData("Sistem Operasi", $_POST['os']);
            echo tampilkanData("Tingkat PHP", $_POST['tingkat']);
            echo "</table>";

            if (count($bahasa) > 2) {
                echo "<p class='text-success'>Anda cukup berpengalaman dalam pemrograman!</p>";
            }
        } else {
            echo "<p class='text-danger'>Semua input wajib diisi!</p>";
        }
    }
    ?>
</div>
</body>
</html>