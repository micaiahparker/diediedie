?game: stat+

stat: "stat" string roll pairs  
pairs: "{" pair* "}"
pair: string ":" string

roll: number "d" number colmod? mod?
mod: op number
colmod: colop number

op:   "+" -> add_
    | "-" -> sub_
    | "*" -> mul_
    | "/" -> div_

colop: "l" -> min_
      | "m" -> max_

string: ESCAPED_STRING
number: INT

COMMENT: /\#[^\n]*/

%import common.INT
%import common.ESCAPED_STRING
%import common.WORD
%import common.WS
%ignore WS
%ignore COMMENT