<?php

// Asignaciones
$var1 = 10;
$var2 = 20.5;
$var3 = "Hola, mundo";

// Operaciones aritméticas
$suma = $var1 + $var2;
$resta = $var1 - $var2;
$multiplicacion = $var1 * $var2;
$division = $var1 / $var2;
$modulo = $var1 % 3;

// Comparaciones
if ($x > 10) {
    echo "Mayor que 10";
} elseif ($x == 10) {
    echo "Es igual a 10";
} else {
    echo "Menor que 10";
}



// Estructuras de control
for ($i = 0; $i < 5; $i++) {
    echo "Iteración: $i\n";
}


while ($var1 > 0) {
    echo "Decrementando var1:";
}

switch ($var3) {
    case "Hola, mundo":
        echo "Mensaje de saludo detectado";
        break;
    case "Adiós":
        echo "Mensaje de despedida detectado";
        break;
    default:
        echo "Mensaje no reconocido";
        break;
}


?>
