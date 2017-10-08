?start: mod+

mod: type string requirements? bonuses?

type: "class" -> cls
	| "race" -> race

requirements: "requirements" expr+
bonuses: "bonuses" (stat number)+

expr: stat comp number

comp: ">" -> gt
	| "<" -> lt
	| ">=" -> gte
	| "<=" -> lte

stat: "int" -> int
	| "wis" -> wis
	| "dex" -> dex
	| "con" -> con
	| "cha" -> cha
	| "str" -> str

string: ESCAPED_STRING
number: SIGNED_NUMBER

%import common.SIGNED_NUMBER
%import common.ESCAPED_STRING
%import common.WS
%ignore WS