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

### The first 1000 Untouchable numbers:
```
Enter a list of numbers separated by space: 
2 5 52 88 96 120 124 146 162 188 206 210 216 238
 246 248 262 268 290 292 304 322 324 334 336 342
 348 354 366 376 382 384 402 406 408 426 438 444
 446 456 464 472 474 476 486 488 492 496 502 510
 516 520 522 532 534 536 540 552 556 558 562 564
 568 570 572 576 588 592 594 606 610 612 616 620 
622 624 634 636 642 648 650 652 654 658 660 666 668 
672 678 680 690 692 696 702 708 714 720 726 732 738 
740 744 748 750 754 756 762 766 774 778 780 792 796 
798 804 810 812 816 818 820 822 824 834 836 846 852 
856 858 860 868 876 880 882 888 894 896 902 906 910 
912 918 920 924 926 930 934 936 940 942 946 948 952 
954 960 962 966 970 972 978 984 986 990 992 996 1002
+------------+------------+------------+------------+---------------+
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
+------------+------------+------------+------------+---------------+
|     2      |     1      |     1      |    1.25    |       0       |
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
|    124     |     60     |     6      |     31     |       1       |
+------------+------------+------------+------------+---------------+
|    146     |     72     |     9      |     37     |       1       |
+------------+------------+------------+------------+---------------+
|    162     |     54     |     9      |     28     |       0       |
+------------+------------+------------+------------+---------------+
|    188     |     92     |     2      |     24     |       0       |
+------------+------------+------------+------------+---------------+
|    206     |    102     |     3      |    26.5    |       1       |
+------------+------------+------------+------------+---------------+
|    210     |     48     |     3      |     13     |       1       |
+------------+------------+------------+------------+---------------+
|    216     |     72     |     9      |     37     |       1       |
+------------+------------+------------+------------+---------------+
|    238     |     96     |     6      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    246     |     80     |     8      |     41     |       1       |
+------------+------------+------------+------------+---------------+
|    248     |    120     |     3      |     31     |       1       |
+------------+------------+------------+------------+---------------+
|    262     |    130     |     4      |    33.5    |       1       |
+------------+------------+------------+------------+---------------+
|    268     |    132     |     6      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    290     |    112     |     4      |     29     |       1       |
+------------+------------+------------+------------+---------------+
|    292     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    304     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    322     |    132     |     6      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    324     |    108     |     9      |     55     |       0       |
+------------+------------+------------+------------+---------------+
|    334     |    166     |     4      |    42.5    |       1       |
+------------+------------+------------+------------+---------------+
|    336     |     96     |     6      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    342     |    108     |     9      |     55     |       0       |
+------------+------------+------------+------------+---------------+
|    348     |    112     |     4      |     29     |       1       |
+------------+------------+------------+------------+---------------+
|    354     |    116     |     8      |     59     |       1       |
+------------+------------+------------+------------+---------------+
|    366     |    120     |     3      |     31     |       1       |
+------------+------------+------------+------------+---------------+
|    376     |    184     |     4      |     47     |       1       |
+------------+------------+------------+------------+---------------+
|    382     |    190     |     1      |    48.5    |       1       |
+------------+------------+------------+------------+---------------+
|    384     |    128     |     2      |     33     |       0       |
+------------+------------+------------+------------+---------------+
|    402     |    132     |     6      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    406     |    168     |     6      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    408     |    128     |     2      |     33     |       0       |
+------------+------------+------------+------------+---------------+
|    426     |    140     |     5      |     71     |       1       |
+------------+------------+------------+------------+---------------+
|    438     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    444     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    446     |    222     |     6      |    112     |       0       |
+------------+------------+------------+------------+---------------+
|    456     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    464     |    224     |     8      |    113     |       1       |
+------------+------------+------------+------------+---------------+
|    472     |    232     |     7      |    117     |       0       |
+------------+------------+------------+------------+---------------+
|    474     |    156     |     3      |     40     |       0       |
+------------+------------+------------+------------+---------------+
|    476     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    486     |    162     |     9      |     82     |       0       |
+------------+------------+------------+------------+---------------+
|    488     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    492     |    160     |     7      |     81     |       0       |
+------------+------------+------------+------------+---------------+
|    496     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    502     |    250     |     7      |    126     |       0       |
+------------+------------+------------+------------+---------------+
|    510     |    128     |     2      |     33     |       0       |
+------------+------------+------------+------------+---------------+
|    516     |    168     |     6      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    520     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    522     |    168     |     6      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    532     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    534     |    176     |     5      |     89     |       1       |
+------------+------------+------------+------------+---------------+
|    536     |    264     |     3      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    540     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    552     |    176     |     5      |     89     |       1       |
+------------+------------+------------+------------+---------------+
|    556     |    276     |     6      |    139     |       1       |
+------------+------------+------------+------------+---------------+
|    558     |    180     |     9      |     91     |       0       |
+------------+------------+------------+------------+---------------+
|    562     |    280     |     1      |     71     |       1       |
+------------+------------+------------+------------+---------------+
|    564     |    184     |     4      |     47     |       1       |
+------------+------------+------------+------------+---------------+
|    568     |    280     |     1      |     71     |       1       |
+------------+------------+------------+------------+---------------+
|    570     |    144     |     9      |     73     |       1       |
+------------+------------+------------+------------+---------------+
|    572     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    576     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    588     |    168     |     6      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    592     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    594     |    180     |     9      |     91     |       0       |
+------------+------------+------------+------------+---------------+
|    606     |    200     |     2      |     51     |       0       |
+------------+------------+------------+------------+---------------+
|    610     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    612     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    616     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    620     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    622     |    310     |     4      |    78.5    |       1       |
+------------+------------+------------+------------+---------------+
|    624     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    634     |    316     |     1      |     80     |       0       |
+------------+------------+------------+------------+---------------+
|    636     |    208     |     1      |     53     |       1       |
+------------+------------+------------+------------+---------------+
|    642     |    212     |     5      |    107     |       1       |
+------------+------------+------------+------------+---------------+
|    648     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    650     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    652     |    324     |     9      |    163     |       1       |
+------------+------------+------------+------------+---------------+
|    654     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    658     |    276     |     6      |    139     |       1       |
+------------+------------+------------+------------+---------------+
|    660     |    160     |     7      |     81     |       0       |
+------------+------------+------------+------------+---------------+
|    666     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    668     |    332     |     8      |    167     |       1       |
+------------+------------+------------+------------+---------------+
|    672     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    678     |    224     |     8      |    113     |       1       |
+------------+------------+------------+------------+---------------+
|    680     |    256     |     4      |     65     |       0       |
+------------+------------+------------+------------+---------------+
|    690     |    176     |     5      |     89     |       1       |
+------------+------------+------------+------------+---------------+
|    692     |    344     |     2      |     87     |       0       |
+------------+------------+------------+------------+---------------+
|    696     |    224     |     8      |    113     |       1       |
+------------+------------+------------+------------+---------------+
|    702     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    708     |    232     |     7      |    117     |       0       |
+------------+------------+------------+------------+---------------+
|    714     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    720     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    726     |    220     |     4      |     56     |       0       |
+------------+------------+------------+------------+---------------+
|    732     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    738     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    740     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    744     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    748     |    320     |     5      |    161     |       0       |
+------------+------------+------------+------------+---------------+
|    750     |    200     |     2      |     51     |       0       |
+------------+------------+------------+------------+---------------+
|    754     |    336     |     3      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    756     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    762     |    252     |     9      |    127     |       1       |
+------------+------------+------------+------------+---------------+
|    766     |    382     |     4      |    96.5    |       1       |
+------------+------------+------------+------------+---------------+
|    774     |    252     |     9      |    127     |       1       |
+------------+------------+------------+------------+---------------+
|    778     |    388     |     1      |     98     |       0       |
+------------+------------+------------+------------+---------------+
|    780     |    192     |     3      |     49     |       0       |
+------------+------------+------------+------------+---------------+
|    792     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    796     |    396     |     9      |    199     |       1       |
+------------+------------+------------+------------+---------------+
|    798     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    804     |    264     |     3      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    810     |    216     |     9      |    109     |       1       |
+------------+------------+------------+------------+---------------+
|    812     |    336     |     3      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    816     |    256     |     4      |     65     |       0       |
+------------+------------+------------+------------+---------------+
|    818     |    408     |     3      |    103     |       1       |
+------------+------------+------------+------------+---------------+
|    820     |    320     |     5      |    161     |       0       |
+------------+------------+------------+------------+---------------+
|    822     |    272     |     2      |     69     |       0       |
+------------+------------+------------+------------+---------------+
|    824     |    408     |     3      |    103     |       1       |
+------------+------------+------------+------------+---------------+
|    834     |    276     |     6      |    139     |       1       |
+------------+------------+------------+------------+---------------+
|    836     |    360     |     9      |    181     |       1       |
+------------+------------+------------+------------+---------------+
|    846     |    276     |     6      |    139     |       1       |
+------------+------------+------------+------------+---------------+
|    852     |    280     |     1      |     71     |       1       |
+------------+------------+------------+------------+---------------+
|    856     |    424     |     1      |    107     |       1       |
+------------+------------+------------+------------+---------------+
|    858     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    860     |    336     |     3      |     85     |       0       |
+------------+------------+------------+------------+---------------+
|    868     |    360     |     9      |    181     |       1       |
+------------+------------+------------+------------+---------------+
|    876     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    880     |    320     |     5      |    161     |       0       |
+------------+------------+------------+------------+---------------+
|    882     |    252     |     9      |    127     |       1       |
+------------+------------+------------+------------+---------------+
|    888     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    894     |    296     |     8      |    149     |       1       |
+------------+------------+------------+------------+---------------+
|    896     |    384     |     6      |    193     |       1       |
+------------+------------+------------+------------+---------------+
|    902     |    400     |     4      |    101     |       1       |
+------------+------------+------------+------------+---------------+
|    906     |    300     |     3      |     76     |       0       |
+------------+------------+------------+------------+---------------+
|    910     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    912     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    918     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    920     |    352     |     1      |     89     |       1       |
+------------+------------+------------+------------+---------------+
|    924     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    926     |    462     |     3      |   116.5    |       1       |
+------------+------------+------------+------------+---------------+
|    930     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    934     |    466     |     7      |    234     |       0       |
+------------+------------+------------+------------+---------------+
|    936     |    288     |     9      |    145     |       0       |
+------------+------------+------------+------------+---------------+
|    940     |    368     |     8      |    185     |       0       |
+------------+------------+------------+------------+---------------+
|    942     |    312     |     6      |    157     |       1       |
+------------+------------+------------+------------+---------------+
|    946     |    420     |     6      |    211     |       1       |
+------------+------------+------------+------------+---------------+
|    948     |    312     |     6      |    157     |       1       |
+------------+------------+------------+------------+---------------+
|    952     |    384     |     6      |    193     |       1       |
+------------+------------+------------+------------+---------------+
|    954     |    312     |     6      |    157     |       1       |
+------------+------------+------------+------------+---------------+
|    960     |    256     |     4      |     65     |       0       |
+------------+------------+------------+------------+---------------+
|    962     |    432     |     9      |    217     |       0       |
+------------+------------+------------+------------+---------------+
|    966     |    264     |     3      |     67     |       1       |
+------------+------------+------------+------------+---------------+
|    970     |    384     |     6      |    193     |       1       |
+------------+------------+------------+------------+---------------+
|    972     |    324     |     9      |    163     |       1       |
+------------+------------+------------+------------+---------------+
|    978     |    324     |     9      |    163     |       1       |
+------------+------------+------------+------------+---------------+
|    984     |    320     |     5      |    161     |       0       |
+------------+------------+------------+------------+---------------+
|    986     |    448     |     7      |    225     |       0       |
+------------+------------+------------+------------+---------------+
|    990     |    240     |     6      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    992     |    480     |     3      |    121     |       0       |
+------------+------------+------------+------------+---------------+
|    996     |    328     |     4      |     83     |       1       |
+------------+------------+------------+------------+---------------+
|    1002    |    332     |     8      |    167     |       1       |
+------------+------------+------------+------------+---------------+
```

### Let's filter the list and show which numbers share the same Totients, Totient Sum and the same Prime Number:

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