
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND ARRAY ARROW ARROWMAP AS BOOL BOOLEAN BREAK CASE CATCH CLASS CLONE CLOSETAG COLON COMMA CONCATENATEEQUAL CONST CONTINUE DECLARE DEFAULT DIVIDE DO DOT DOUBLEDOT DOUBLEMINUS DOUBLEPLUS ECHO ELSE ELSEIF EMPTY ENDSWITCH EQ EQUALS EXCEPTION EXTENDS FALSE FGETS FINAL FINALLY FLOAT FLOATING FN FOR FOREACH FUNCTION GEQ GLOBAL GT ID IF IMPLEMENTS INCLUDE INSTANCEOF INT INTEGER INTERFACE ISSET LBRACE LBRACKET LEQ LIST LPAREN LT MINUS MINUSEQUAL MODULO NAMESPACE NEQ NEW NOT OPENTAG OR PLUS PLUSEQUAL POTENCIA PRINT PRIVATE PROTECTED PUBLIC QUESTION RBRACE RBRACKET RETURN RPAREN SEMICOLON STATIC STDIN STRICTEQ STRICTNEQ STRING STRINGS SWITCH THIS THROW TIMES TRUE TRY VARIABLE VOID WHILEprograma : sentencia\n                | sentencia programasentencia : asignacion\n                | impresion\n                | comparacion\n                | estructurasProgramsentencias : sentencia\n                  | sentencia sentencias\n                  | emptyasignacion : VARIABLE EQUALS operaArit SEMICOLONimpresion : ECHO imprimir SEMICOLON\n                | PRINT imprimir SEMICOLONestructurasProgram : controlStructure\n                            | dataStructure\n                            | funcionDeclarate\n                            | classDeclaratecontrolStructure : if\n                        | for\n                        | while\n                        | switchif : statementif ELSE body\n          | statementif ELSE if\n          | statementif ELSEIF if\n          | statementifstatementif : IF LPAREN conditionProdu RPAREN LBRACE body RBRACEconditionProdu : condition\n                    | condition opLogic conditionProducondition : valor opSymbol valor\n                 | LPAREN conditionProdu RPARENopSymbol : EQ\n                | NEQ\n                | STRICTEQ\n                | STRICTNEQ\n                | LT\n                | GT\n                | LEQ\n                | GEQopLogic : AND\n                | OR\n                | NOTfor : forStatementforStatement : FOR LPAREN forcondition RPAREN LBRACE body RBRACEforcondition : VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEPLUS\n                    | VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEMINUSwhile : WHILE LPAREN condition RPAREN LBRACE body RBRACE\n             | WHILE LPAREN condition RPAREN LBRACE RBRACEswitch : SWITCH LPAREN condition RPAREN LBRACE caseLists RBRACE\n              | SWITCH LPAREN condition RPAREN LBRACE RBRACEcaseLists : cases default\n                | cases\n                | default\n                | emptycases : case cases\n             | casecase : CASE valor COLON body BREAK SEMICOLONdefault : DEFAULT COLON body BREAK SEMICOLONdataStructure : array\n                    | mapfuncionDeclarate : FUNCTION ID LPAREN parametros RPAREN LBRACE funcionBody RBRACE\n                        | FUNCTION ID LPAREN parametros RPAREN DOUBLEDOT dataType LBRACE funcionBody RBRACEfuncionBody : body\n                   | RETURN expresion SEMICOLONparametros : parametro\n                 | parametro COMMA parametros\n                 | emptyparametro : ID\n                | dataType ID\n                | ID EQUALS valor\n                | dataType ID EQUALS valorarrowfunction : FN LPAREN parametros RPAREN ARROWMAP expresion SEMICOLONbrace : LBRACE body RBRACEfuncionParen : ID LPAREN parametros RPARENfuncionAnonima : VARIABLE EQUALS FUNCTION LPAREN parametros RPAREN LBRACE RETURN expresion SEMICOLON RBRACE SEMICOLONclassDeclarate : CLASS ID LBRACE classBody RBRACE\n                      | CLASS ID EXTENDS ID LBRACE classBody RBRACEclassBody : classMember classBody\n                 | emptyclassMember : dataType VARIABLE SEMICOLON\n                   | dataType FUNCTION ID LPAREN parametros RPAREN braceaccessMember : VARIABLE ARROW ID\n                    | VARIABLE ARROW funcionParenarray : VARIABLE EQUALS LBRACKET repiteValores RBRACKET SEMICOLON\n             | VARIABLE EQUALS ARRAY LPAREN repiteValores RPAREN SEMICOLON\n             | VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON\n             | VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLONmap : VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON\n            | VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLONmapProduc : mapArrow\n                 | mapArrow COMMA mapProducmapArrow : valor ARROWMAP valorbody : sentencia\n            | sentencia sentencias\n            | emptyimprimir : LPAREN repiteValores RPAREN\n                | LPAREN RPAREN\n                | repiteValoresvalor : INT\n            | FLOAT\n            | VARIABLE\n            | STRING\n            | TRUE\n            | FALSE\n            | THIS\n            | funcionParen\n            | funcionAnonimadataType : INTEGER\n                | FLOATING\n                | STRINGS\n                | BOOLEAN\n                | VOIDcomparacion : INT operador INT\n                    | FLOAT operador FLOAT\n                    | INT operador FLOAT\n                    | FLOAT operador INTrepiteValores : valor COMMA repiteValores\n                     | valoroperaArit : valor\n                |  valor operador operaArit\n                | valor DOT valorexpresion : valor\n                 | operaArit\n                 | conditionProdu\n                 | ternario\n                 | accessMemberoperador :  PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODULOternario : conditionProdu QUESTION expresion COLON expresionempty :'
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,8,9,12,13,14,15,16,17,18,19,20,21,24,25,31,33,48,49,50,51,52,56,58,59,60,61,63,66,69,72,73,74,75,76,80,81,82,83,84,85,93,98,99,100,109,110,111,112,113,118,120,121,122,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,156,161,163,166,168,170,171,180,181,187,189,195,198,199,200,205,208,209,210,213,215,216,219,227,230,232,234,245,247,250,252,],[7,7,-3,-4,-5,-6,38,38,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,38,38,-125,-126,-127,-128,-129,7,38,38,38,92,38,-11,38,-12,-111,-113,-112,-114,-21,-17,7,-93,-23,38,-10,38,38,38,-106,-107,-108,-109,-110,158,7,-92,-9,38,-30,-31,-32,-33,-34,-35,-36,-37,38,-38,-39,-40,38,38,38,-74,-8,7,7,7,-82,-85,38,7,-46,-48,38,217,-83,-84,226,-75,-45,-47,7,-25,-42,-59,7,7,226,226,-60,7,255,226,]),'ECHO':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[8,8,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,8,-11,-12,-111,-113,-112,-114,-21,-17,8,-93,-23,-10,8,-92,-9,-74,-8,8,8,8,-82,-85,8,-46,-48,-83,-84,-75,-45,-47,8,-25,-42,-59,8,8,-60,8,]),'PRINT':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[9,9,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,9,-11,-12,-111,-113,-112,-114,-21,-17,9,-93,-23,-10,9,-92,-9,-74,-8,9,9,9,-82,-85,9,-46,-48,-83,-84,-75,-45,-47,9,-25,-42,-59,9,9,-60,9,]),'INT':([0,2,3,4,5,6,8,9,12,13,14,15,16,17,18,19,20,21,24,25,31,33,47,48,49,50,51,52,53,56,58,59,60,63,66,69,72,73,74,75,76,80,81,82,83,84,85,93,98,99,100,120,121,122,125,126,127,128,129,130,131,132,133,136,137,138,139,141,144,145,151,156,161,163,166,168,170,171,180,181,187,189,195,199,200,205,208,209,210,213,215,216,219,227,230,231,232,234,245,247,252,],[10,10,-3,-4,-5,-6,36,36,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,36,36,73,-125,-126,-127,-128,-129,76,10,36,36,36,36,-11,36,-12,-111,-113,-112,-114,-21,-17,10,-93,-23,36,-10,36,36,36,10,-92,-9,36,-30,-31,-32,-33,-34,-35,-36,-37,36,-38,-39,-40,169,36,36,36,-74,-8,10,10,10,-82,-85,36,10,-46,-48,36,-83,-84,36,-75,-45,-47,10,-25,-42,-59,10,10,240,36,36,-60,10,36,]),'FLOAT':([0,2,3,4,5,6,8,9,12,13,14,15,16,17,18,19,20,21,24,25,31,33,47,48,49,50,51,52,53,56,58,59,60,63,66,69,72,73,74,75,76,80,81,82,83,84,85,93,98,99,100,120,121,122,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,156,161,163,166,168,170,171,180,181,187,189,195,199,200,205,208,209,210,213,215,216,219,227,230,232,234,245,247,252,],[11,11,-3,-4,-5,-6,37,37,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,37,37,74,-125,-126,-127,-128,-129,75,11,37,37,37,37,-11,37,-12,-111,-113,-112,-114,-21,-17,11,-93,-23,37,-10,37,37,37,11,-92,-9,37,-30,-31,-32,-33,-34,-35,-36,-37,37,-38,-39,-40,37,37,37,-74,-8,11,11,11,-82,-85,37,11,-46,-48,37,-83,-84,37,-75,-45,-47,11,-25,-42,-59,11,11,37,37,-60,11,37,]),'FUNCTION':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,70,72,73,74,75,76,80,81,82,83,84,93,109,110,111,112,113,118,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[22,22,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,22,-11,103,-12,-111,-113,-112,-114,-21,-17,22,-93,-23,-10,-106,-107,-108,-109,-110,159,22,-92,-9,-74,-8,22,22,22,-82,-85,22,-46,-48,-83,-84,-75,-45,-47,22,-25,-42,-59,22,22,-60,22,]),'CLASS':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[23,23,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,23,-11,-12,-111,-113,-112,-114,-21,-17,23,-93,-23,-10,23,-92,-9,-74,-8,23,23,23,-82,-85,23,-46,-48,-83,-84,-75,-45,-47,23,-25,-42,-59,23,23,-60,23,]),'WHILE':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[26,26,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,26,-11,-12,-111,-113,-112,-114,-21,-17,26,-93,-23,-10,26,-92,-9,-74,-8,26,26,26,-82,-85,26,-46,-48,-83,-84,-75,-45,-47,26,-25,-42,-59,26,26,-60,26,]),'SWITCH':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[27,27,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,27,-11,-12,-111,-113,-112,-114,-21,-17,27,-93,-23,-10,27,-92,-9,-74,-8,27,27,27,-82,-85,27,-46,-48,-83,-84,-75,-45,-47,27,-25,-42,-59,27,27,-60,27,]),'IF':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,57,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[28,28,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,28,28,-11,-12,-111,-113,-112,-114,-21,-17,28,-93,-23,-10,28,-92,-9,-74,-8,28,28,28,-82,-85,28,-46,-48,-83,-84,-75,-45,-47,28,-25,-42,-59,28,28,-60,28,]),'FOR':([0,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,163,166,168,170,171,181,187,189,199,200,208,209,210,213,215,216,219,227,230,245,247,],[29,29,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,29,-11,-12,-111,-113,-112,-114,-21,-17,29,-93,-23,-10,29,-92,-9,-74,-8,29,29,29,-82,-85,29,-46,-48,-83,-84,-75,-45,-47,29,-25,-42,-59,29,29,-60,29,]),'$end':([1,2,3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,30,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,170,171,187,189,199,200,208,209,210,215,216,219,245,],[0,-1,-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,-2,-131,-11,-12,-111,-113,-112,-114,-21,-17,-91,-93,-23,-10,-7,-92,-9,-74,-8,-82,-85,-46,-48,-83,-84,-75,-45,-47,-25,-42,-59,-60,]),'RBRACE':([3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,78,80,81,82,83,84,93,115,116,117,120,121,122,156,157,160,161,163,165,166,168,170,171,181,183,185,186,187,188,189,190,191,192,193,196,197,199,200,203,204,208,209,210,211,212,215,216,219,227,233,236,245,246,247,248,251,253,254,258,],[-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,-131,-11,-12,-111,-113,-112,-114,-131,-21,-17,-91,-93,-23,-10,156,-131,-77,-7,-92,-9,-74,-76,-131,-8,187,189,-131,-131,-82,-85,-131,-78,208,209,-46,210,-48,-50,-51,-52,-54,215,216,-83,-84,219,-61,-75,-45,-47,-49,-53,-25,-42,-59,-131,-62,245,-60,-79,-131,-56,256,258,-55,-71,]),'BREAK':([3,4,5,6,12,13,14,15,16,17,18,19,20,21,24,25,56,66,72,73,74,75,76,80,81,82,83,84,93,120,121,122,156,161,170,171,187,189,199,200,208,209,210,213,215,216,219,229,230,239,245,],[-3,-4,-5,-6,-13,-14,-15,-16,-17,-18,-19,-20,-57,-58,-24,-41,-131,-11,-12,-111,-113,-112,-114,-21,-17,-91,-93,-23,-10,-7,-92,-9,-74,-8,-82,-85,-46,-48,-83,-84,-75,-45,-47,-131,-25,-42,-59,238,-131,249,-60,]),'EQUALS':([7,38,92,104,154,226,],[31,70,141,151,180,70,]),'LPAREN':([8,9,26,27,28,29,45,54,58,59,60,64,85,103,136,137,138,139,184,205,232,234,243,252,],[33,33,58,59,60,61,71,77,85,85,85,98,85,150,85,-38,-39,-40,207,85,85,85,71,85,]),'STRING':([8,9,31,33,48,49,50,51,52,58,59,60,63,69,85,98,99,100,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,180,195,205,232,234,252,],[39,39,39,39,-125,-126,-127,-128,-129,39,39,39,39,39,39,39,39,39,39,-30,-31,-32,-33,-34,-35,-36,-37,39,-38,-39,-40,39,39,39,39,39,39,39,39,39,]),'TRUE':([8,9,31,33,48,49,50,51,52,58,59,60,63,69,85,98,99,100,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,180,195,205,232,234,252,],[40,40,40,40,-125,-126,-127,-128,-129,40,40,40,40,40,40,40,40,40,40,-30,-31,-32,-33,-34,-35,-36,-37,40,-38,-39,-40,40,40,40,40,40,40,40,40,40,]),'FALSE':([8,9,31,33,48,49,50,51,52,58,59,60,63,69,85,98,99,100,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,180,195,205,232,234,252,],[41,41,41,41,-125,-126,-127,-128,-129,41,41,41,41,41,41,41,41,41,41,-30,-31,-32,-33,-34,-35,-36,-37,41,-38,-39,-40,41,41,41,41,41,41,41,41,41,]),'THIS':([8,9,31,33,48,49,50,51,52,58,59,60,63,69,85,98,99,100,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,151,180,195,205,232,234,252,],[42,42,42,42,-125,-126,-127,-128,-129,42,42,42,42,42,42,42,42,42,42,-30,-31,-32,-33,-34,-35,-36,-37,42,-38,-39,-40,42,42,42,42,42,42,42,42,42,]),'ID':([8,9,22,23,31,33,48,49,50,51,52,58,59,60,63,69,71,77,79,85,98,99,100,108,109,110,111,112,113,125,126,127,128,129,130,131,132,133,136,137,138,139,144,145,150,151,153,159,180,195,205,207,232,234,235,252,],[45,45,54,55,45,45,-125,-126,-127,-128,-129,45,45,45,45,45,104,104,119,45,45,45,45,154,-106,-107,-108,-109,-110,45,-30,-31,-32,-33,-34,-35,-36,-37,45,-38,-39,-40,45,45,104,45,104,184,45,45,45,104,45,45,243,45,]),'PLUS':([10,11,36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[48,48,-97,-98,-99,-100,-101,-102,-103,-104,-105,48,-72,48,-99,-73,]),'MINUS':([10,11,36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[49,49,-97,-98,-99,-100,-101,-102,-103,-104,-105,49,-72,49,-99,-73,]),'TIMES':([10,11,36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[50,50,-97,-98,-99,-100,-101,-102,-103,-104,-105,50,-72,50,-99,-73,]),'DIVIDE':([10,11,36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[51,51,-97,-98,-99,-100,-101,-102,-103,-104,-105,51,-72,51,-99,-73,]),'MODULO':([10,11,36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[52,52,-97,-98,-99,-100,-101,-102,-103,-104,-105,52,-72,52,-99,-73,]),'ELSE':([24,215,],[56,-25,]),'ELSEIF':([24,215,],[57,-25,]),'LBRACKET':([31,],[63,]),'ARRAY':([31,],[64,]),'SEMICOLON':([32,34,35,36,37,38,39,40,41,42,43,44,46,62,65,68,90,101,102,142,143,148,149,152,158,162,164,167,169,175,176,220,221,222,223,224,225,226,238,240,241,243,244,249,256,257,261,],[66,-96,-116,-97,-98,-99,-100,-101,-102,-103,-104,-105,72,93,-117,-95,-26,-94,-115,170,171,-118,-119,-72,183,-29,-28,-27,198,199,200,233,-117,-121,-122,-123,-124,-99,248,250,251,-80,-81,254,261,-130,-73,]),'RPAREN':([33,35,36,37,38,39,40,41,42,43,44,67,71,77,86,88,89,90,91,96,97,102,104,105,106,107,114,123,146,147,150,152,153,154,162,164,167,172,173,177,178,179,202,207,228,259,260,261,],[68,-116,-97,-98,-99,-100,-101,-102,-103,-104,-105,101,-131,-131,124,134,135,-26,140,-116,-88,-115,-66,152,-63,-65,155,162,175,176,-131,-72,-131,-67,-29,-28,-27,-90,-89,201,-68,-64,-69,-131,237,-43,-44,-73,]),'COMMA':([35,36,37,38,39,40,41,42,43,44,96,97,104,106,152,154,172,178,202,261,],[69,-97,-98,-99,-100,-101,-102,-103,-104,-105,69,145,-66,153,-72,-67,-90,-68,-69,-73,]),'RBRACKET':([35,36,37,38,39,40,41,42,43,44,94,95,96,97,102,152,172,173,261,],[-116,-97,-98,-99,-100,-101,-102,-103,-104,-105,142,143,-116,-88,-115,-72,-90,-89,-73,]),'DOT':([36,37,38,39,40,41,42,43,44,65,152,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,100,-72,100,-99,-73,]),'EQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,126,-72,126,126,-99,-73,]),'NEQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,127,-72,127,127,-99,-73,]),'STRICTEQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,128,-72,128,128,-99,-73,]),'STRICTNEQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,129,-72,129,129,-99,-73,]),'LT':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,130,-72,130,130,-99,-73,]),'GT':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,131,-72,131,131,-99,-73,]),'LEQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,132,-72,132,132,-99,-73,]),'GEQ':([36,37,38,39,40,41,42,43,44,87,152,217,221,226,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,133,-72,133,133,-99,-73,]),'ARROWMAP':([36,37,38,39,40,41,42,43,44,96,152,174,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,144,-72,144,-73,]),'COLON':([36,37,38,39,40,41,42,43,44,65,90,148,149,152,162,164,167,194,214,221,222,223,224,225,226,242,243,244,257,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,-117,-26,-118,-119,-72,-29,-28,-27,213,230,-117,-121,-122,-123,-124,-99,252,-80,-81,-130,-73,]),'AND':([36,37,38,39,40,41,42,43,44,90,152,162,164,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,137,-72,-29,-28,-73,]),'OR':([36,37,38,39,40,41,42,43,44,90,152,162,164,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,138,-72,-29,-28,-73,]),'NOT':([36,37,38,39,40,41,42,43,44,90,152,162,164,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,139,-72,-29,-28,-73,]),'QUESTION':([36,37,38,39,40,41,42,43,44,90,152,162,164,167,223,261,],[-97,-98,-99,-100,-101,-102,-103,-104,-105,-26,-72,-29,-28,-27,234,-73,]),'LBRACE':([55,109,110,111,112,113,119,124,134,135,140,155,201,206,237,],[78,-106,-107,-108,-109,-110,160,163,165,166,168,181,218,227,247,]),'EXTENDS':([55,],[79,]),'INTEGER':([71,77,78,116,150,153,160,182,183,207,246,258,],[109,109,109,109,109,109,109,109,-78,109,-79,-71,]),'FLOATING':([71,77,78,116,150,153,160,182,183,207,246,258,],[110,110,110,110,110,110,110,110,-78,110,-79,-71,]),'STRINGS':([71,77,78,116,150,153,160,182,183,207,246,258,],[111,111,111,111,111,111,111,111,-78,111,-79,-71,]),'BOOLEAN':([71,77,78,116,150,153,160,182,183,207,246,258,],[112,112,112,112,112,112,112,112,-78,112,-79,-71,]),'VOID':([71,77,78,116,150,153,160,182,183,207,246,258,],[113,113,113,113,113,113,113,113,-78,113,-79,-71,]),'DOUBLEDOT':([155,],[182,]),'DEFAULT':([165,190,193,212,254,],[194,194,-54,-53,-55,]),'CASE':([165,193,254,],[195,195,-55,]),'RETURN':([181,218,227,],[205,232,205,]),'ARROW':([226,],[235,]),'DOUBLEPLUS':([255,],[259,]),'DOUBLEMINUS':([255,],[260,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,],[1,30,]),'sentencia':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[2,2,82,120,120,82,82,82,82,82,82,82,82,]),'asignacion':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[3,3,3,3,3,3,3,3,3,3,3,3,3,]),'impresion':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[4,4,4,4,4,4,4,4,4,4,4,4,4,]),'comparacion':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'estructurasProgram':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'controlStructure':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[12,12,12,12,12,12,12,12,12,12,12,12,12,]),'dataStructure':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'funcionDeclarate':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[14,14,14,14,14,14,14,14,14,14,14,14,14,]),'classDeclarate':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'if':([0,2,56,57,82,120,163,166,168,181,213,227,230,247,],[16,16,81,84,16,16,16,16,16,16,16,16,16,16,]),'for':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[17,17,17,17,17,17,17,17,17,17,17,17,17,]),'while':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[18,18,18,18,18,18,18,18,18,18,18,18,18,]),'switch':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[19,19,19,19,19,19,19,19,19,19,19,19,19,]),'array':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[20,20,20,20,20,20,20,20,20,20,20,20,20,]),'map':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[21,21,21,21,21,21,21,21,21,21,21,21,21,]),'statementif':([0,2,56,57,82,120,163,166,168,181,213,227,230,247,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'forStatement':([0,2,56,82,120,163,166,168,181,213,227,230,247,],[25,25,25,25,25,25,25,25,25,25,25,25,25,]),'imprimir':([8,9,],[32,46,]),'repiteValores':([8,9,33,63,69,98,],[34,34,67,94,102,146,]),'valor':([8,9,31,33,58,59,60,63,69,85,98,99,100,125,136,144,145,151,180,195,205,232,234,252,],[35,35,65,35,87,87,87,96,35,87,96,65,149,164,87,172,174,178,202,214,221,221,221,221,]),'funcionParen':([8,9,31,33,58,59,60,63,69,85,98,99,100,125,136,144,145,151,180,195,205,232,234,235,252,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,244,43,]),'funcionAnonima':([8,9,31,33,58,59,60,63,69,85,98,99,100,125,136,144,145,151,180,195,205,232,234,252,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'operador':([10,11,65,221,],[47,53,99,99,]),'operaArit':([31,99,205,232,234,252,],[62,148,222,222,222,222,]),'body':([56,163,166,168,181,213,227,230,247,],[80,186,196,197,204,229,204,239,253,]),'empty':([56,71,77,78,82,116,120,150,153,160,163,165,166,168,181,207,213,227,230,247,],[83,107,107,117,122,117,122,107,107,117,83,192,83,83,83,107,83,83,83,83,]),'condition':([58,59,60,85,136,205,232,234,252,],[86,88,90,90,90,90,90,90,90,]),'conditionProdu':([60,85,136,205,232,234,252,],[89,123,167,223,223,223,223,]),'forcondition':([61,],[91,]),'mapProduc':([63,98,145,],[95,147,173,]),'mapArrow':([63,98,145,],[97,97,97,]),'parametros':([71,77,150,153,207,],[105,114,177,179,228,]),'parametro':([71,77,150,153,207,],[106,106,106,106,106,]),'dataType':([71,77,78,116,150,153,160,182,207,],[108,108,118,118,108,108,118,206,108,]),'classBody':([78,116,160,],[115,157,185,]),'classMember':([78,116,160,],[116,116,116,]),'sentencias':([82,120,],[121,161,]),'opSymbol':([87,217,221,],[125,231,125,]),'opLogic':([90,],[136,]),'caseLists':([165,],[188,]),'cases':([165,193,],[190,212,]),'default':([165,190,],[191,211,]),'case':([165,193,],[193,193,]),'funcionBody':([181,227,],[203,236,]),'expresion':([205,232,234,252,],[220,241,242,257,]),'ternario':([205,232,234,252,],[224,224,224,224,]),'accessMember':([205,232,234,252,],[225,225,225,225,]),'brace':([237,],[246,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> sentencia','programa',1,'p_programa','main.py',6),
  ('programa -> sentencia programa','programa',2,'p_programa','main.py',7),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','main.py',10),
  ('sentencia -> impresion','sentencia',1,'p_sentencia','main.py',11),
  ('sentencia -> comparacion','sentencia',1,'p_sentencia','main.py',12),
  ('sentencia -> estructurasProgram','sentencia',1,'p_sentencia','main.py',13),
  ('sentencias -> sentencia','sentencias',1,'p_sentencias','main.py',16),
  ('sentencias -> sentencia sentencias','sentencias',2,'p_sentencias','main.py',17),
  ('sentencias -> empty','sentencias',1,'p_sentencias','main.py',18),
  ('asignacion -> VARIABLE EQUALS operaArit SEMICOLON','asignacion',4,'p_asignacion','main.py',21),
  ('impresion -> ECHO imprimir SEMICOLON','impresion',3,'p_impresion','main.py',26),
  ('impresion -> PRINT imprimir SEMICOLON','impresion',3,'p_impresion','main.py',27),
  ('estructurasProgram -> controlStructure','estructurasProgram',1,'p_estructurasProgram','main.py',33),
  ('estructurasProgram -> dataStructure','estructurasProgram',1,'p_estructurasProgram','main.py',34),
  ('estructurasProgram -> funcionDeclarate','estructurasProgram',1,'p_estructurasProgram','main.py',35),
  ('estructurasProgram -> classDeclarate','estructurasProgram',1,'p_estructurasProgram','main.py',36),
  ('controlStructure -> if','controlStructure',1,'p_controlStructure','main.py',39),
  ('controlStructure -> for','controlStructure',1,'p_controlStructure','main.py',40),
  ('controlStructure -> while','controlStructure',1,'p_controlStructure','main.py',41),
  ('controlStructure -> switch','controlStructure',1,'p_controlStructure','main.py',42),
  ('if -> statementif ELSE body','if',3,'p_if','main.py',46),
  ('if -> statementif ELSE if','if',3,'p_if','main.py',47),
  ('if -> statementif ELSEIF if','if',3,'p_if','main.py',48),
  ('if -> statementif','if',1,'p_if','main.py',49),
  ('statementif -> IF LPAREN conditionProdu RPAREN LBRACE body RBRACE','statementif',7,'p_statementif','main.py',52),
  ('conditionProdu -> condition','conditionProdu',1,'p_conditionProdu','main.py',55),
  ('conditionProdu -> condition opLogic conditionProdu','conditionProdu',3,'p_conditionProdu','main.py',56),
  ('condition -> valor opSymbol valor','condition',3,'p_condition','main.py',58),
  ('condition -> LPAREN conditionProdu RPAREN','condition',3,'p_condition','main.py',59),
  ('opSymbol -> EQ','opSymbol',1,'p_opSymbol','main.py',62),
  ('opSymbol -> NEQ','opSymbol',1,'p_opSymbol','main.py',63),
  ('opSymbol -> STRICTEQ','opSymbol',1,'p_opSymbol','main.py',64),
  ('opSymbol -> STRICTNEQ','opSymbol',1,'p_opSymbol','main.py',65),
  ('opSymbol -> LT','opSymbol',1,'p_opSymbol','main.py',66),
  ('opSymbol -> GT','opSymbol',1,'p_opSymbol','main.py',67),
  ('opSymbol -> LEQ','opSymbol',1,'p_opSymbol','main.py',68),
  ('opSymbol -> GEQ','opSymbol',1,'p_opSymbol','main.py',69),
  ('opLogic -> AND','opLogic',1,'p_opLogic','main.py',71),
  ('opLogic -> OR','opLogic',1,'p_opLogic','main.py',72),
  ('opLogic -> NOT','opLogic',1,'p_opLogic','main.py',73),
  ('for -> forStatement','for',1,'p_for','main.py',77),
  ('forStatement -> FOR LPAREN forcondition RPAREN LBRACE body RBRACE','forStatement',7,'p_forStatement','main.py',80),
  ('forcondition -> VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEPLUS','forcondition',10,'p_forcondition','main.py',83),
  ('forcondition -> VARIABLE EQUALS INT SEMICOLON VARIABLE opSymbol INT SEMICOLON VARIABLE DOUBLEMINUS','forcondition',10,'p_forcondition','main.py',84),
  ('while -> WHILE LPAREN condition RPAREN LBRACE body RBRACE','while',7,'p_while','main.py',88),
  ('while -> WHILE LPAREN condition RPAREN LBRACE RBRACE','while',6,'p_while','main.py',89),
  ('switch -> SWITCH LPAREN condition RPAREN LBRACE caseLists RBRACE','switch',7,'p_switch','main.py',92),
  ('switch -> SWITCH LPAREN condition RPAREN LBRACE RBRACE','switch',6,'p_switch','main.py',93),
  ('caseLists -> cases default','caseLists',2,'p_caseLists','main.py',95),
  ('caseLists -> cases','caseLists',1,'p_caseLists','main.py',96),
  ('caseLists -> default','caseLists',1,'p_caseLists','main.py',97),
  ('caseLists -> empty','caseLists',1,'p_caseLists','main.py',98),
  ('cases -> case cases','cases',2,'p_cases','main.py',100),
  ('cases -> case','cases',1,'p_cases','main.py',101),
  ('case -> CASE valor COLON body BREAK SEMICOLON','case',6,'p_case','main.py',103),
  ('default -> DEFAULT COLON body BREAK SEMICOLON','default',5,'p_default','main.py',105),
  ('dataStructure -> array','dataStructure',1,'p_dataStructure','main.py',108),
  ('dataStructure -> map','dataStructure',1,'p_dataStructure','main.py',109),
  ('funcionDeclarate -> FUNCTION ID LPAREN parametros RPAREN LBRACE funcionBody RBRACE','funcionDeclarate',8,'p_funcionDeclarate','main.py',112),
  ('funcionDeclarate -> FUNCTION ID LPAREN parametros RPAREN DOUBLEDOT dataType LBRACE funcionBody RBRACE','funcionDeclarate',10,'p_funcionDeclarate','main.py',113),
  ('funcionBody -> body','funcionBody',1,'p_funcionBody','main.py',115),
  ('funcionBody -> RETURN expresion SEMICOLON','funcionBody',3,'p_funcionBody','main.py',116),
  ('parametros -> parametro','parametros',1,'p_parametros','main.py',119),
  ('parametros -> parametro COMMA parametros','parametros',3,'p_parametros','main.py',120),
  ('parametros -> empty','parametros',1,'p_parametros','main.py',121),
  ('parametro -> ID','parametro',1,'p_parametro','main.py',123),
  ('parametro -> dataType ID','parametro',2,'p_parametro','main.py',124),
  ('parametro -> ID EQUALS valor','parametro',3,'p_parametro','main.py',125),
  ('parametro -> dataType ID EQUALS valor','parametro',4,'p_parametro','main.py',126),
  ('arrowfunction -> FN LPAREN parametros RPAREN ARROWMAP expresion SEMICOLON','arrowfunction',7,'p_arrowfunction','main.py',128),
  ('brace -> LBRACE body RBRACE','brace',3,'p_brace','main.py',131),
  ('funcionParen -> ID LPAREN parametros RPAREN','funcionParen',4,'p_funcionParen','main.py',134),
  ('funcionAnonima -> VARIABLE EQUALS FUNCTION LPAREN parametros RPAREN LBRACE RETURN expresion SEMICOLON RBRACE SEMICOLON','funcionAnonima',12,'p_funcionAnonima','main.py',137),
  ('classDeclarate -> CLASS ID LBRACE classBody RBRACE','classDeclarate',5,'p_classDeclarate','main.py',141),
  ('classDeclarate -> CLASS ID EXTENDS ID LBRACE classBody RBRACE','classDeclarate',7,'p_classDeclarate','main.py',142),
  ('classBody -> classMember classBody','classBody',2,'p_classBody','main.py',144),
  ('classBody -> empty','classBody',1,'p_classBody','main.py',145),
  ('classMember -> dataType VARIABLE SEMICOLON','classMember',3,'p_classMember','main.py',147),
  ('classMember -> dataType FUNCTION ID LPAREN parametros RPAREN brace','classMember',7,'p_classMember','main.py',148),
  ('accessMember -> VARIABLE ARROW ID','accessMember',3,'p_accessMember','main.py',150),
  ('accessMember -> VARIABLE ARROW funcionParen','accessMember',3,'p_accessMember','main.py',151),
  ('array -> VARIABLE EQUALS LBRACKET repiteValores RBRACKET SEMICOLON','array',6,'p_array','main.py',154),
  ('array -> VARIABLE EQUALS ARRAY LPAREN repiteValores RPAREN SEMICOLON','array',7,'p_array','main.py',155),
  ('array -> VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON','array',7,'p_array','main.py',156),
  ('array -> VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON','array',6,'p_array','main.py',157),
  ('map -> VARIABLE EQUALS LBRACKET mapProduc RBRACKET SEMICOLON','map',6,'p_map','main.py',160),
  ('map -> VARIABLE EQUALS ARRAY LPAREN mapProduc RPAREN SEMICOLON','map',7,'p_map','main.py',161),
  ('mapProduc -> mapArrow','mapProduc',1,'p_mapProduc','main.py',164),
  ('mapProduc -> mapArrow COMMA mapProduc','mapProduc',3,'p_mapProduc','main.py',165),
  ('mapArrow -> valor ARROWMAP valor','mapArrow',3,'p_mapArrow','main.py',168),
  ('body -> sentencia','body',1,'p_body','main.py',171),
  ('body -> sentencia sentencias','body',2,'p_body','main.py',172),
  ('body -> empty','body',1,'p_body','main.py',173),
  ('imprimir -> LPAREN repiteValores RPAREN','imprimir',3,'p_imprimir','main.py',176),
  ('imprimir -> LPAREN RPAREN','imprimir',2,'p_imprimir','main.py',177),
  ('imprimir -> repiteValores','imprimir',1,'p_imprimir','main.py',178),
  ('valor -> INT','valor',1,'p_valor','main.py',182),
  ('valor -> FLOAT','valor',1,'p_valor','main.py',183),
  ('valor -> VARIABLE','valor',1,'p_valor','main.py',184),
  ('valor -> STRING','valor',1,'p_valor','main.py',185),
  ('valor -> TRUE','valor',1,'p_valor','main.py',186),
  ('valor -> FALSE','valor',1,'p_valor','main.py',187),
  ('valor -> THIS','valor',1,'p_valor','main.py',188),
  ('valor -> funcionParen','valor',1,'p_valor','main.py',189),
  ('valor -> funcionAnonima','valor',1,'p_valor','main.py',190),
  ('dataType -> INTEGER','dataType',1,'p_dataType','main.py',194),
  ('dataType -> FLOATING','dataType',1,'p_dataType','main.py',195),
  ('dataType -> STRINGS','dataType',1,'p_dataType','main.py',196),
  ('dataType -> BOOLEAN','dataType',1,'p_dataType','main.py',197),
  ('dataType -> VOID','dataType',1,'p_dataType','main.py',198),
  ('comparacion -> INT operador INT','comparacion',3,'p_comparacion','main.py',201),
  ('comparacion -> FLOAT operador FLOAT','comparacion',3,'p_comparacion','main.py',202),
  ('comparacion -> INT operador FLOAT','comparacion',3,'p_comparacion','main.py',203),
  ('comparacion -> FLOAT operador INT','comparacion',3,'p_comparacion','main.py',204),
  ('repiteValores -> valor COMMA repiteValores','repiteValores',3,'p_repiteValores','main.py',209),
  ('repiteValores -> valor','repiteValores',1,'p_repiteValores','main.py',210),
  ('operaArit -> valor','operaArit',1,'p_operaArit','main.py',212),
  ('operaArit -> valor operador operaArit','operaArit',3,'p_operaArit','main.py',213),
  ('operaArit -> valor DOT valor','operaArit',3,'p_operaArit','main.py',214),
  ('expresion -> valor','expresion',1,'p_expresion','main.py',216),
  ('expresion -> operaArit','expresion',1,'p_expresion','main.py',217),
  ('expresion -> conditionProdu','expresion',1,'p_expresion','main.py',218),
  ('expresion -> ternario','expresion',1,'p_expresion','main.py',219),
  ('expresion -> accessMember','expresion',1,'p_expresion','main.py',220),
  ('operador -> PLUS','operador',1,'p_operador','main.py',222),
  ('operador -> MINUS','operador',1,'p_operador','main.py',223),
  ('operador -> TIMES','operador',1,'p_operador','main.py',224),
  ('operador -> DIVIDE','operador',1,'p_operador','main.py',225),
  ('operador -> MODULO','operador',1,'p_operador','main.py',226),
  ('ternario -> conditionProdu QUESTION expresion COLON expresion','ternario',5,'p_ternario','main.py',228),
  ('empty -> <empty>','empty',0,'p_empty','main.py',232),
]
