<?php
// Validar arreglos asociativos
$persona = array("nombre" => "Piero", "edad" => 25, "ciudad" => "Lima");

// Acceso a datos del arreglo asociativo
echo $persona["nombre"]; // Deberia imprimir: Piero

// Validar if-else
$edad = 18;
if ($edad >= 18) {
    echo "Eres mayor de edad.";
} else {
    echo "Eres menor de edad.";
}

// Validar funcion anonima
$multiplicar = function($a, $b) {
    return $a * $b;
};
echo $multiplicar(3, 4); // Deberia imprimir: 12
?>
