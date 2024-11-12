<?php

// Definimos una interfaz para las operaciones matemáticas
interface Operacion {
    public function calcular($num1, $num2);
}

// Clase para la operación de suma
class Suma implements Operacion {
    public function calcular($num1, $num2) {
        return $num1 + $num2;
    }
}

// Clase para la operación de resta
class Resta implements Operacion {
    public function calcular($num1, $num2) {
        return $num1 - $num2;
    }
}

// Clase para la operación de multiplicación
class Multiplicacion implements Operacion {
    public function calcular($num1, $num2) {
        return $num1 * $num2;
    }
}

// Clase para la operación de división con manejo de excepción si el divisor es cero
class Division implements Operacion {
    public function calcular($num1, $num2) {
        if ($num2 == 0) {
            throw new Exception("Error: División por cero no permitida.");
        }
        return $num1 / $num2;
    }
}

// Clase Calculadora que usa el patrón de diseño 'Factory' para crear operaciones
class Calculadora {
    const OPERACIONES = [
        'suma' => 'Suma',
        'resta' => 'Resta',
        'multiplicacion' => 'Multiplicacion',
        'division' => 'Division'
    ];

    public function realizarOperacion($tipo, $num1, $num2) {
        if (!array_key_exists($tipo, self::OPERACIONES)) {
            throw new Exception("Error: Operación no soportada.");
        }

        // Creamos una instancia de la operación solicitada
        $operacionClase = self::OPERACIONES[$tipo];
        $operacion = new $operacionClase();
        return $operacion->calcular($num1, $num2);
    }
}

// Ejemplo de uso
$calculadora = new Calculadora();
$numeros = [10, 5];

$operaciones = ['suma', 'resta', 'multiplicacion', 'division'];
foreach ($operaciones as $op) {
    try {
        $resultado = $calculadora->realizarOperacion($op, $numeros[0], $numeros[1]);
        echo "Resultado de la operación $op entre {$numeros[0]} y {$numeros[1]}: $resultado\n";
    } catch (Exception $e) {
        echo $e->getMessage() . "\n";
    }
}

?>
