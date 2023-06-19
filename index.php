<!DOCTYPE html>
<html>
<head>
    <title>Pesquisa por Frequência</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        
        th, td {
            border: 1px solid black;
            padding: 8px;
        }
        
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<!DOCTYPE html>
<html>
<head>
 

<title>Pesquisa de Valor em Arquivo TXT</title>
</head>
<body>
  <h1>Pesquisa de Valor em Arquivo TXT</h1>

  <form method="POST">
    <label for="valor">Digite o valor a pesquisar:</label>
    <input type="text" name="valor" id="valor" required>
    <button type="submit">Pesquisar</button>
  </form>

  <?php
  if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $valorDesejado = $_POST['valor'];
    $conteudo = file_get_contents('freq-a23.txt');
    $linhas = explode("\n", $conteudo);
    echo "kHz           Time(UTC) Days  ITU Station                Lang. Target   Remarks" . "\n";
    foreach ($linhas as $linha) {
      if (preg_match("/\b$valorDesejado\b/", $linha)) {
        echo $linha . "<br>";
      }
    }
  }
  ?>

</body>
</html>

<body>
    <h1>Pesquisa por Frequência</h1>
    <?php
        $date = gmdate("Y-m-d H:i:s"); // Obtém a data e hora internacional
        echo '<p>Data e hora internacional: ' . $date . '</p>';
    ?>
    <form method="GET">
        <label for="search">Pesquisar Frequência:</label>
        <input type="text" name="search" id="search" placeholder="escreva aqui">
        <input type="submit" value="pesquisar">
    </form>

    <?php
    if (!empty($_GET['search'])) {
        $search = $_GET['search'];
        $results = [];
        
        $file = fopen('sked-a23.csv', 'r');
        
        if ($file) {
            $header = fgetcsv($file, 0, "\t");
            
            $frequencyColumnIndex = array_search('kHz:75', $header);
            
            while ($row = fgetcsv($file, 0, "\t")) {
                $frequency = $row[$frequencyColumnIndex];
                
                if (stripos($frequency, $search) !== false) {
                    $results[] = $row;
                }
            }
            
            fclose($file);
        }
        
        if (!empty($results)) {
            echo '<h2>Resultados para a frequência "'.$search.'":</h2>';
            
            echo '<table>';
            echo '<tr>';
            foreach ($header as $column) {
                echo '<th>'.$column.'</th>';
            }
            echo '</tr>';
            
            foreach ($results as $result) {
                echo '<tr>';
                foreach ($result as $value) {
                    echo '<td>'.$value.'</td>';
                }
                echo '</tr>';
            }
            
            echo '</table>';
        } else {
            echo 'Nenhum resultado encontrado para a frequência "'.$search.'".';
        }
    }
    ?>
</body>
</html>
