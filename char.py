from functools import wraps
import lark

def unpack(m, values):
    return [values[i] if i < len(values) else None for i in range(m)]

class Class_:
    def __init__(self, values):
        name, *buckets = values

class Race:
    def __init__(self, values):
        name, *buckets = values


class GameTransfomer(lark.Transformer):
    string = lambda x, y: y[0][1:-1]
    class_ = Class_
    race = Race

with open('char.g') as fd:
    parser = lark.Lark(fd.read(), start="game", parser='lalr', transformer=GameTransfomer())

if __name__ == "__main__":   
    with open('example.game') as fd:
        tree = parser.parse(fd.read())
        print(tree)