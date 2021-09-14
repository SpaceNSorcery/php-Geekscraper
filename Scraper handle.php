$ composer init --require="php >7.4" --no-interaction
$ composer update
<?php

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://www.dndbeyond.com/spells');

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');

curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

$response = curl_exec($ch);

echo 'HTTP Status Code: ' . curl_getinfo($ch, CURLINFO_HTTP_CODE) .PHP_EOL;
echo 'Response Body: '  . $response . PHP_EOL;

curl_close($ch);
