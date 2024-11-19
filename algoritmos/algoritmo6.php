<?php
// Prueba de estructura de control while
while ($x < 10) {
    echo $x;
    $x++;
}

// Prueba de switch
switch ($variable) {
    case 1:
        echo "Es uno";
        break;
    case 2:
        echo "Es dos";
        break;
    default:
        echo "No es ni uno ni dos";
        break;
}

// Declaración de una función
function suma($a, $b) {
    return $a + $b;
}

// Declaración de una función con tipo de retorno
function resta(int $a, int $b): int {
    return $a - $b;
}

// Declaración de una clase
class Persona {
    public $nombre;
    private $edad;

    function __construct($nombre, $edad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
    }

    public function getNombre() {
        return $this->nombre;
    }

    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }
}

// Instanciación de un objeto
$persona = new Persona("Moises", 25);
echo $persona->getNombre();

// Acceso a un miembro de la clase
$persona->setNombre("Alvarez");
echo $persona->getNombre();

// Declaración de un array
$array = [1, 2, 3];

// Declaración de un mapa
$mapa = [
    "clave1" => "valor1",
    "clave2" => "valor2"
];

// Función anónima
$sumaAnonima = function($a, $b) {
    return $a + $b;
};
echo $sumaAnonima(10, 20);
?>
