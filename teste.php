<?php $handle = fopen("teste.csv", "r");$row = 0;
while ($line = fgetcsv($handle, 1000, ",")) {
	if ($row++ == 0) {
		continue;
	}
	
	$people[] = [
		'palvra' => $line[0],
		'aumentativo' => $line[1],
		'diminutivo' => $line[2]
		
	];
}print_r($people);fclose($handle); ?>