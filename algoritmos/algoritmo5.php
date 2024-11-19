<?php

// Declaración de un array con algunos valores
$numeros = array(1, 2, 3, 4, 5);

// Asignación de valores a variables
$x = 10;
$y = 20;
$z = 30;

// Uso de una sentencia if para comparar valores
if ($x == $y) {
    echo "x es igual a y.\n";
} elseif ($x < $y) {
    echo "x es menor que y.\n";
} else {
    echo "x es mayor que y.\n";
}

// Comprobación manual de si el número 3 está en el array
$encontrado = false;
foreach ($numeros as $numero) {
    if ($numero == 3) {
        $encontrado = true;
        break;  // Salimos del bucle tan pronto como encontramos el número
    }
}

if ($encontrado) {
    echo "El número 3 está en el array.\n";
} else {
    echo "El número 3 no está en el array.\n";
}

// Recorrido del array usando foreach (sin while)
echo "Recorriendo el array:\n";
foreach ($numeros as $numero) {
    echo "Valor: " . $numero . "\n";
}
?>
