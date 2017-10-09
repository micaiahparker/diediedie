from functools import wraps, partial
from operator import add, sub, mul
from heapq import nlargest, nsmallest
from random import randint

import lark


def unpack(m, values):
    return [values[i] if i < len(values) else None for i in range(m)]

class Modifier:
    def __init__(self, values):
        self.op, self.value = unpack(2, values)
        self.op = partial(self.op, self.value)

    def __call__(self, value):
        return self.op(value)

class Roll:
    def __init__(self, values):
        self.times, self.size, self.colmod, self.mod = unpack(4, values)

        if not self.mod:
            self.mod = lambda x: x

        if not self.colmod:
            self.colmod = lambda x: x

    def __call__(self):
        return self.mod(sum(self.colmod([randint(1,self.size) for _ in range(self.times)])))


class GameTransfomer(lark.Transformer):
    string = lambda x, y: y[0][1:-1]
    number = lambda x, y: int(y[0])
    min_ = lambda x, y: nsmallest
    max_ = lambda x, y: nlargest
    add_ = lambda x, y: add
    sub_ = lambda x, y: sub
    mul_ = lambda x, y: mul
    div_ = lambda x, y: divmod
    mod = Modifier
    colmod = Modifier
    roll = Roll

with open('char.g') as fd:
    parser = lark.Lark(fd.read(), start="game", parser='lalr', transformer=GameTransfomer())

if __name__ == "__main__":   
    with open('example.game') as fd:
        tree = parser.parse(fd.read())
        print(tree.pretty())