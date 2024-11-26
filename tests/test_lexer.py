import pytest
from AnalizadorLexPHP import lexer

# Función auxiliar para procesar datos con el lexer
def tokenize(data):
    lexer.input(data)
    return [tok for tok in lexer]

# Test: Detección de palabras reservadas
def test_reserved_keywords():
    data = "abstract and array as break case class const default do echo else"
    tokens = tokenize(data)
    expected_types = [
        "ABSTRACT", "AND", "ARRAY", "AS", "BREAK", "CASE", 
        "CLASS", "CONST", "DEFAULT", "DO", "ECHO", "ELSE"
    ]
    assert [tok.type for tok in tokens] == expected_types

# Test: Detección de operadores
def test_operators():
    data = "+ - * / ** % += -= .= == === != !== < > <= >="
    tokens = tokenize(data)
    expected_types = [
        "PLUS", "MINUS", "TIMES", "DIVIDE", "POTENCIA", "MODULO", 
        "PLUSEQUAL", "MINUSEQUAL", "CONCATENATEEQUAL", 
        "EQ", "STRICTEQ", "NEQ", "STRICTNEQ", 
        "LT", "GT", "LEQ", "GEQ"
    ]
    assert [tok.type for tok in tokens] == expected_types

# Test: Detección de delimitadores y signos de puntuación
def test_delimiters():
    data = "( ) { } [ ] ; , . => ->"
    tokens = tokenize(data)
    expected_types = [
        "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
        "LBRACKET", "RBRACKET", "SEMICOLON", 
        "COMMA", "DOT", "ARROWMAP", "ARROW"
    ]
    assert [tok.type for tok in tokens] == expected_types

# Test: Detección de variables
def test_variables():
    data = "$var1 $var2 $variableName"
    tokens = tokenize(data)
    expected_values = ["$var1", "$var2", "$variableName"]
    assert [tok.type for tok in tokens] == ["VARIABLE", "VARIABLE", "VARIABLE"]
    assert [tok.value for tok in tokens] == expected_values

# Test: Detección de enteros y flotantes
def test_numbers():
    data = "42 3.14159 0.001"
    tokens = tokenize(data)
    expected_types = ["INT", "FLOAT", "FLOAT"]
    expected_values = [42, 3.14159, 0.001]
    assert [tok.type for tok in tokens] == expected_types
    assert [tok.value for tok in tokens] == expected_values

# Test: Detección de cadenas
def test_strings():
    data = '"Hello, World!" \'This is a test\''
    tokens = tokenize(data)
    expected_types = ["STRING", "STRING"]
    expected_values = ["Hello, World!", "This is a test"]
    assert [tok.type for tok in tokens] == expected_types
    assert [tok.value for tok in tokens] == expected_values

# Test: Detección de palabras reservadas booleanas
def test_booleans():
    data = "True False true false"
    tokens = tokenize(data)
    expected_types = ["BOOL", "BOOL", "BOOL", "BOOL"]
    expected_values = [True, False, True, False]
    assert [tok.type for tok in tokens] == expected_types
    assert [tok.value for tok in tokens] == expected_values


# Test: Manejo de caracteres ilegales
def test_illegal_character():
    data = "@ #"
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    assert len(tokens) == 0  # No se generan tokens para caracteres ilegales

# Test: Manejo de comentarios
def test_comments():
    data = """
    // Esto es un comentario de línea
    /* Esto es un comentario 
       multilínea */
    """
    lexer.input(data)
    tokens = list(lexer)
    assert len(tokens) == 0  # Los comentarios no deben generar tokens

# Test: Manejo de etiquetas PHP
def test_php_tags():
    data = "<?php ?> <?php echo 'Hello'; ?>"
    tokens = tokenize(data)
    expected_types = ["OPENTAG", "CLOSETAG", "OPENTAG", "ECHO", "STRING", "SEMICOLON", "CLOSETAG"]
    assert [tok.type for tok in tokens] == expected_types
def test_null_token():
    data = "$var = NULL; $otherVar = null;"
    tokens = tokenize(data)
    expected_types = ["VARIABLE", "EQUALS", "NULL", "SEMICOLON", "VARIABLE", "EQUALS", "NULL", "SEMICOLON"]
    expected_values = ["$var", "=", "NULL", ";", "$otherVar", "=", "null", ";"]
    
    # Comprobar los tipos de los tokens
    assert [tok.type for tok in tokens] == expected_types
    
    # Comprobar los valores de los tokens
    assert [tok.value for tok in tokens] == expected_values
