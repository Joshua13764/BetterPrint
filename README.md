# BetterPrint
Adds a better print function

## Settings for bPrint

### List settings

#### ```zfillList```

_Will zfill each element in the list with the specified zfill number_

example code: ```bprint([i for i in range(10)], zfillList=5)```

output: ```[00000, 00001, 00002, 00003, 00004, 00005, 00006, 00007, 00008, 00009]```

#### ```headers```

_Will output the data in a table format_

example code: ```bprint([['John', 38], ['Amy', 24]], headers=['Name', 'Age'], tablefmt='orgtbl')```

output:
```
| Name   |   Age |
|--------+-------|
| John   |    38 |
| Amy    |    24 |
```

