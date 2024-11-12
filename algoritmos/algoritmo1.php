<?php
// Ejemplo de variables y asignaciones
$variable1 = 10;
$variable2 = 20.5;
$cadena = "Hola, mundo!";
$booleano = true;

// Operadores aritméticos
$suma = $variable1 + $variable2;
$resta = $variable1 - $variable2;
$multiplicacion = $variable1 * 3;
$division = $variable2 / $variable1;
$modulo = $variable1 % 3;

// Operadores de comparación
$esIgual = ($variable1 == $variable2);
$esIdentico = ($variable1 === 10);
$esMenor = ($variable1 < $variable2);
$esMayor = ($variable1 > $variable2);
$esDiferente = ($variable1 != $variable2);

// Estructuras de control
if ($variable1 > 5) {
    echo "Variable 1 es mayor que 5\n";
} elseif ($variable1 == 5) {
    echo "Variable 1 es igual a 5\n";
} else {
    echo "Variable 1 es menor que 5\n";
}

for ($i = 0; $i < 5; $i++) {
    echo "Iteración: $i\n";
}

// Operadores lógicos
$esVerdadero = ($booleano && ($variable1 > 5)) || !$booleano;

// Comentarios de una línea
# Otro comentario de una línea

/*
Comentario de múltiples líneas
que abarca más de una línea
*/

// Ejemplo de función
function suma($a, $b) {
    return $a + $b;
}

// Ejemplo de llamada a función
$resultado = suma($variable1, $variable2);
echo "Resultado de la suma: $resultado\n";

// Operadores de concatenación y asignación compuesta
$cadena .= " ¡Bienvenido!";
$variable1 += 5;
?>
