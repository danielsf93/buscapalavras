<?php
$handle = fopen("teste.csv", "r");
$row = 0;
$people = [];

while ($line = fgetcsv($handle, 1000, ",")) {
    if ($row++ == 0) {
        continue;
    }

    $people[] = [
        'palavra' => $line[0],
        'aumentativo' => $line[1],
        'diminutivo' => $line[2]
    ];
}

fclose($handle);

// Verificar se a caixa de busca foi preenchida
$searchWord = isset($_GET['search']) ? $_GET['search'] : '';

// Encontrar os resultados correspondentes à palavra pesquisada
$results = [];
foreach ($people as $person) {
    if ($person['palavra'] === $searchWord) {
        $results['aumentativo'] = $person['aumentativo'];
        $results['diminutivo'] = $person['diminutivo'];
        break;
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Busca de Palavras</title>
</head>
<body>
    <form action="" method="get">
        <label for="search">Palavra:</label>
        <input type="text" name="search" id="search" value="<?php echo $searchWord; ?>">
        <input type="submit" value="Buscar">
    </form>

    <?php if (!empty($results)): ?>
        <h2>Resultados para "<?php echo $searchWord; ?>":</h2>
        <p>Aumentativo: <?php echo $results['aumentativo']; ?></p>
        <p>Diminutivo: <?php echo $results['diminutivo']; ?></p>
    <?php endif; ?>
</body>
</html>
