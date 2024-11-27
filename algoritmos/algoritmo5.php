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
switch ($i) {
    case 0:
        echo "i es igual a 0";
        break;
    case 1:
        echo "i es igual a 1";
        break;
    case 2:
        echo "i es igual a 2";
        break;
}

switch ($i) {
    case "manzana":
        echo "i es una manzana";
        break;
    case "barra":
        echo "i es una barra";
        break;
    case "pastel":
        echo "i es un pastel";
        break;
}

switch ($i) {
    case 0:
        echo "i es igual a 0";
    case 1:
        echo "i es igual a 1";
    case 2:
        echo "i es igual a 2";
}
switch ($i) {
    case 0:
    case 1:
    case 2:
        echo "i es menor que 3 pero no negativo";
        break;
    case 3:
        echo "i es 3";
}

switch ($i) {
    case 0:
        echo "i es igual a 0";
        break;
    case 1:
        echo "i es igual a 1";
        break;
    case 2:
        echo "i es igual a 2";
        break;
    default:
       echo "i no es igual a 0, 1 ni 2";
}
switch($beer)
{
    case 'tuborg';
    case 'carlsberg';
    case 'heineken';
        echo 'Buena elección';
    break;
    default;
        echo 'Por favor haga una nueva selección...';
    break;
}

switch ($i):
    case 0:
        echo "i es igual a 0";
        break;
    case 1:
        echo "i es igual a 1";
        break;
    case 2:
        echo "i es igual a 2";
        break;
    default:
        echo "i no es igual a 0, 1 ni 2";
endswitch;

?>
