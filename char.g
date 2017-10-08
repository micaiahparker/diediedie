?game: mod+

?mod: class_ requirements? bonuses?
    | race requirements? bonuses?

class_: "class" string
race: "race" string

requirements: "requirements" expr+
bonuses: "bonuses" (stat number)+

expr: stat comp number

comp: ">" -> gt
    | "<" -> lt
    | ">=" -> gte
    | "<=" -> lte

stat: "int" -> int_
    | "wis" -> wis_
    | "dex" -> dex_
    | "con" -> con_
    | "cha" -> cha_
    | "str" -> str_

?string: ESCAPED_STRING
?number: SIGNED_NUMBER

COMMENT: /\#[^\n]*/

%import common.SIGNED_NUMBER
%import common.ESCAPED_STRING
%import common.WORD
%import common.WS
%ignore WS
%ignore COMMENT