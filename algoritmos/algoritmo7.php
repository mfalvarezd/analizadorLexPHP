<?php 

$valor = 5;

$resultado = (2 == $valor) ? 'Sí' : 'No'; // $resultado se establece en 'No'
$resultado = (5 == $valor) ? 'Sí' : 'No'; // $resultado se establece en 'Sí'
echo (5 == $valor) ? 'Sí' : 'No'; // 'Sí' se imprimirá

// desde PHP 5.3
$valorTexto = 'Texto Aquí';
$resultado = ($valorTexto) ?: 'Sin Valor'; // $resultado se establece en 'Texto Aquí'

$valorNum = 0;

while ($valorNum < 3) { // Cambiado para que sea un ciclo válido
    echo "Incrementando valorNum:"; // Esto imprime en cada iteración
    $valorNum++;
}

// Error sintáctico: falta el case '2:' en la segunda sentencia switch
switch ($indice) {
    case 0:
        echo "índice es igual a 0";
        break;
    case 1:
        echo "índice es igual a 1";
        break;
    // case 2: // Esta línea está intencionadamente comentada para provocar un error
        echo "índice es igual a 2";
        break;
}

switch ($fruta) {
    case "pera":
        echo "fruta es una pera";
        break;
    case "naranja":
        echo "fruta es una naranja";
        break;
    case "uva":
        echo "fruta es una uva";
        break;
}

switch ($numero) {
    case 0:
        echo "numero es igual a 0";
    case 1: // Falta el break aquí para provocar un error semántico
        echo "numero es igual a 1";
    case 2:
        echo "numero es igual a 2";
        break;
}

switch ($numero) {
    case 0:
    case 1:
    case 2:
        echo "numero es menor que 3 pero no negativo";
        break;
    case 4: // Error semántico: se añade un caso incorrecto
        echo "numero es 4";
}

switch ($bebida) {
    case 'cerveza';
    case 'vino';
    case 'whisky';
        echo 'Buena elección';
    break;
    default: // Error léxico: el uso incorrecto de un `;` en lugar de `:`
        echo 'Por favor, elige de nuevo...';
    break;
}

switch ($indice):
    case 0:
        echo "índice es igual a 0";
        break;
    case 1:
        echo "índice es igual a 1";
        break;
    case 2:
        echo "índice es igual a 2";
        break;
    default:
        echo "índice no es igual a 0, 1 ni 2";
endswitch;

?>
