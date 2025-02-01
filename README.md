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

#### ```plot```

_Will output the data as a plt pyplot_

example code: ```bprint([i for i in range(10)], [i * 1.2 + 0.3 for i in range(10)], plot="scatter")```

output:
```A straight line plot```

#### ```timeStamp```

_Will add the time stamp to the start of the printout_

example code: ```bprint("Timestamp test", timeStamp=True)```

output:
```2025-02-01 15:49:21.968759      Timestamp test```

#### ```savePath```

_Will log the output to the designated log_

example code: ```bprint("Timestamp test", savePath="log1.log")```

output (in created log1.log file):
```2025-02-01 15:49:21.967054	Timestamp test```


#### ```dictTable```

_Will dictionary as a table of keys and values_

example code: ```bprint({i : chr(i) for i in range(80, 84)}, dictTable = True)```

output (in created log1.log file):
```
keys  values
------  --------
    80  P
    81  Q
    82  R
    83  S
```


