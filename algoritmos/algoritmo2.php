<?php
// Variables y asignaciones básicas
$var1 = 1;
$var2 = 0.5;
$var3=100;
$result = $var1 + $var2 + $var3; // Suma de enteros y flotantes

// Cadenas con secuencias de escape
$string1 = "Hello\nWorld!";
$string2 = 'This is a \t tab.';
$escaped = "She said, \"Hello!\"";

// Operadores de comparación
$isEqual = ($var1 == $var2);
$isNotEqual = ($var1 !== $var2);
$isGreaterOrEqual = ($var1 >= $var2);

// Estructuras de control
if ($var1 < $var2) {
    echo "var1 es menor que var2";
} else {
    echo "var1 es mayor o igual a var2";
}

// Bucles y palabras reservadas
for ($i = 0; $i < 4; $i++) {
    echo "i: $i\n";
}

$array = array(1, 2, 3); // Creación de un arreglo
foreach ($array as $item) {
    echo $item;
}

// Prueba de operadores lógicos
$isTrue = true && false || true;

// Comentarios
// Esto es un comentario de una línea
/* Y esto es un comentario
   de varias líneas */

// Prueba de constantes booleanas y nulas
$isNull = NULL;
$isFalse = false;
$isTrue = true;
?>
