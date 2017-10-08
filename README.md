# diediedie
the easy way to encode your game

`python char.py`

```
game
  mod
    Class: Fighter
    requirements
      expr
        str_
        gt
        10
    bonuses
      cha_
      -1
  mod
    Class: Thief
    requirements
      expr
        dex_
        gt
        11
      expr
        str_
        lt
        17
  mod
    Race: Human
    bonuses
      int_
      1
      str_
      1
      con_
      1
```


