<?php
// Error Léxico: uso de un carácter no permitido ($@)
$variable_invalida$@ = 10; 

// Error Sintáctico: falta un punto y coma (;) al final de la línea
if ($variable_invalida > 5) 
    echo "La variable es mayor que 5" // Falta el punto y coma

// Error Semántico: usar una variable no definida
echo $no_definida_variable; 

function suma($a, $b) {
    return $a + $b;
}

// Semántico: llamada de función con tipos incorrectos
$resultado = suma("texto", 5); // "texto" no es un número

?>
