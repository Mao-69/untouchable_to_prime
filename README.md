# Calculate prime numbers from the set of untouchable numbers

``` 2, 5, 52, 88, 96, 120, 124, 146, 162, 188, 206, 210, 216, 238, 246, 248, 262, 268, 276, 288, 290, 292, 304, 306, 322, 324, 326, 336, 342, 372, 406, 408, 426, 430, 448, 472, 474, 498 ```


let (n) be an integer &gt; 2
in the untouchable numbers set (2,5,52,88,96, . . . , 498)

such that,

the totient number

&Phi;(n) = n&prod;(1-1/p)

is the positive integers up to a given integer (n)
that are relatively prime to (n)

now let,

F₁₀&Phi;(n) be the single digit sum of the totient number,

then let,

&mu; = { 2, if F₁₀&Phi;(n) &ge; 5 or 4, if F₁₀&Phi;(n) &le; 5

such that,

( &Phi;(n) / &mu; ) +1

is a prime number

```shell
python3 ./untouchable_to_prime.py
```


- Numbers that share the same Totient,
Totient Sums and Prime Number 17:
```
| Number | Totient | Digit Sum | Result | Is Prime | 
|--------|---------|-----------|--------|--------- | 
|  96    |  32     |  5        |  17    |    1     |
|  120   |  32     |  5        |  17    |    1     |
```

- Numbers that share the same Totient,
Totient Sums and Prime Number 31:

```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    248     |    120     |     3      |     31     |       1       |
|    366     |    120     |     3      |     31     |       1       |
```

- Numbers that share the same Totient,
Totient Sums and Prime Number 37:

```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 146    | 72      | 9         | 37     | 1        |
| 216    | 72      | 9         | 37     | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 67:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 268    | 132     | 6         | 67     | 1        |
| 322    | 132     | 6         | 67     | 1        |
| 402    | 132     | 6         | 67     | 1        |
| 536    | 264     | 3         | 67     | 1        |
| 804    | 264     | 3         | 67     | 1        |
| 966    | 264     | 3         | 67     | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 71:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 562    | 280     | 1         | 71     | 1        |
| 568    | 280     | 1         | 71     | 1        |
| 852    | 280     | 1         | 71     | 1        |
```


- Numbers that share the same Totients,
Totient Sums and Prime Number 73:
```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    292     |    144     |     9      |     73     |       1       |
|    304     |    144     |     9      |     73     |       1       |
|    438     |    144     |     9      |     73     |       1       |
|    444     |    144     |     9      |     73     |       1       |
|    456     |    144     |     9      |     73     |       1       |
|    540     |    144     |     9      |     73     |       1       |
|    570     |    144     |     9      |     73     |       1       |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 89:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 534    | 176     | 5         | 89     | 1        |
| 690    | 176     | 5         | 89     | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 109:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 648    | 216     | 9         | 109    | 1        |
| 654    | 216     | 9         | 109    | 1        |
| 666    | 216     | 9         | 109    | 1        |
| 702    | 216     | 9         | 109    | 1        |
| 756    | 216     | 9         | 109    | 1        |
| 798    | 216     | 9         | 109    | 1        |
| 810    | 216     | 9         | 109    | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 113:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 678    | 224     | 8         | 113    | 1        |
| 696    | 224     | 8         | 113    | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 127:
```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    762     |    252     |     9      |    127     |       1       |
|    774     |    252     |     9      |    127     |       1       |
|    882     |    252     |     9      |    127     |       1       |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 139:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 658    | 276     | 6         | 139    | 1        |
| 834    | 276     | 6         | 139    | 1        |
| 846    | 276     | 6         | 139    | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 167:
```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    668     |    332     |     8      |    167     |       1       |
|    1002    |    332     |     8      |    167     |       1       |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 181:
```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    836     |    360     |     9      |    181     |       1       |
|    868     |    360     |     9      |    181     |       1       |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 193:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 896    | 384     | 6         | 193    | 1        |
| 952    | 384     | 6         | 193    | 1        |
| 970    | 384     | 6         | 193    | 1        |
```