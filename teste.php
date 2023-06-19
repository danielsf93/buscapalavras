<?php
$valorDesejado = "549";
$conteudo = file_get_contents('freq-a23.txt');
$linhas = explode("\n", $conteudo);
echo "kHz           Time(UTC) Days  ITU Station                Lang. Target   Remarks" . "\n";
foreach ($linhas as $linha) {
  if (preg_match("/\b$valorDesejado\b/", $linha)) {
    
	echo $linha . "\n";
  }
}
?>
