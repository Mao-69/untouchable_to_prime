Calculate prime numbers from the set of untouchable numbers

``` 2, 5, 52, 88, 96, 120, 124, 146, 162, 188, 206, 210, 216, 238, 246, 248, 262, 268, 276, 288, 290, 292, 304, 306, 322, 324, 326, 336, 342, 372, 406, 408, 426, 430, 448, 472, 474, 498 ```


phi;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x

```shell
python3 ./untouchable_to_prime.py
```

```
Enter a list of numbers separated by space: 5 52 88 96 120
+------------+------------+------------+------------+---------------+
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
+------------+------------+------------+------------+---------------+
|     5      |     4      |     4      |     2      |       1       |
+------------+------------+------------+------------+---------------+
|     52     |     24     |     6      |     13     |       1       |
+------------+------------+------------+------------+---------------+
|     88     |     40     |     4      |     11     |       1       |
+------------+------------+------------+------------+---------------+
|     96     |     32     |     5      |     17     |       1       |
+------------+------------+------------+------------+---------------+
|    120     |     32     |     5      |     17     |       1       |
+------------+------------+------------+------------+---------------+
```
