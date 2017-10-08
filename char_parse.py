import lark

with open('dice.g') as fd:
    parser = lark.Lark(fd.read(), start="start")

with open('fighter.mod') as fd:
    tree = parser.parse(fd.read())
