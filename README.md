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

&mu; = { 2, if F₁₀&Phi;(n) ≥ 5 or 4, if F₁₀&Phi;(n) < 5

such that,

( &Phi;(n) / &mu; ) +1

is a prime number

then, 

(n₁, n₂, nₖ) : Φ(n₁) = Φ(n₂) =...= Φ(nₖ) ∧ F₁₀Φ(n₁) = F₁₀Φ(n₂) =...= F₁₀Φ(nₖ) ∧ J(n₁) = J(n₂) =...= J(nₖ)

Are sets of untouchable numbers (n)
where each (n) shares,

the same Totient Φ(n)
Totient-Digit-Sum F₁₀Φ(n)
and the same Prime J(n) = ( Φ(n) / μ ) +1

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
Totient Sums and Prime Number 157:
```
| Number | Totient | Digit Sum | Result | Is Prime |
|--------|---------|-----------|--------|----------|
| 942    | 312     | 6         | 157    | 1        |
| 948    | 312     | 6         | 157    | 1        |
| 954    | 312     | 6         | 157    | 1        |
```

- Numbers that share the same Totients,
Totient Sums and Prime Number 163:
```
|   Number   |  Totient   | Digit Sum  |   Result   |   Is Prime    |
|------------|------------|------------|------------|---------------|
|    972     |    324     |     9      |    163     |       1       |
|    978     |    324     |     9      |    163     |       1       |
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

### Untouchable Twin Pairs
- The Joshie Pairs 🙃

(n₁, n₂, nₖ) : Φ(n₁) = Φ(n₂) =...= Φ(nₖ) ∧ F₁₀Φ(n₁) = F₁₀Φ(n₂) =...= F₁₀Φ(nₖ) ∧ J(n₁) = J(n₂) =...= J(nₖ)

```
{96, 120}
{248, 366}
{146, 216}
{268, 322, 402}
{536, 804, 966}
{562, 568, 852}
{292, 304, 438, 444, 456, 540, 570}
{534, 690}
{648, 654, 666, 702, 756, 798, 810}
{678, 696}
{762, 774, 882}
{658, 834, 846}
{942, 948, 954}
{972, 978}
{668, 1002}
{836, 868}
{896, 952, 970}
```
### They can also be grouped by Vector Magnitudes
### From lower limit 2 to upper limit 6900000 there are 46 magnitudes with exactly two vectors each
```
Magnitude 201:
Vector: [80, 96, 102, 120] with properties: (32, 5, 17)
  Vector components: [80, 96, 102, 120]
  Squares of each component: [6400, 9216, 10404, 14400]
  Sum of squares: 40420
  Magnitude before rounding: 201.0472581260
  The rounded magnitude of the vector is: 201

Vector: [108, 114, 126] with properties: (36, 9, 19)
  Vector components: [108, 114, 126]
  Squares of each component: [11664, 12996, 15876]
  Sum of squares: 40536
  Magnitude before rounding: 201.3355408268
  The rounded magnitude of the vector is: 201

Magnitude 95884:
Vector: [67722, 67878] with properties: (22572, 9, 11287)
  Vector components: [67722, 67878]
  Squares of each component: [4586269284, 4607422884]
  Sum of squares: 9193692168
  Magnitude before rounding: 95883.7429807577
  The rounded magnitude of the vector is: 95884

Vector: [67794, 67806] with properties: (22596, 6, 11299)
  Vector components: [67794, 67806]
  Squares of each component: [4596026436, 4597653636]
  Sum of squares: 9193680072
  Magnitude before rounding: 95883.6799043508
  The rounded magnitude of the vector is: 95884

Magnitude 1119718:
Vector: [126688, 130112, 155792, 156220, 158360, 162640, 183174, 183186, 183276, 184896, 186822, 187464, 190032, 193458, 194740, 195168, 196452, 200304, 207366, 213822, 215712, 229194, 231120, 233688, 234330, 237540, 243960, 250380, 269640, 292110] with properties: (61056, 9, 30529)
  Vector components: [126688, 130112, 155792, 156220, 158360, 162640, 183174, 183186, 183276, 184896, 186822, 187464, 190032, 193458, 194740, 195168, 196452, 200304, 207366, 213822, 215712, 229194, 231120, 233688, 234330, 237540, 243960, 250380, 269640, 292110]
  Squares of each component: [16049849344, 16929132544, 24271147264, 24404688400, 25077889600, 26451769600, 33552714276, 33557110596, 33590092176, 34186530816, 34902459684, 35142751296, 36112161024, 37425997764, 37923667600, 38090548224, 38593388304, 40121692416, 43000657956, 45719847684, 46531666944, 52529889636, 53416454400, 54610081344, 54910548900, 56425251600, 59516481600, 62690144400, 72705729600, 85328252100]
  Sum of squares: 1253768597092
  Magnitude before rounding: 1119718.0882222096
  The rounded magnitude of the vector is: 1119718

Vector: [791754, 791766] with properties: (263916, 9, 131959)
  Vector components: [791754, 791766]
  Squares of each component: [626874396516, 626893398756]
  Sum of squares: 1253767795272
  Magnitude before rounding: 1119717.7301766728
  The rounded magnitude of the vector is: 1119718

Magnitude 1448750:
Vector: [178448, 182936, 196952, 197008, 213668, 223060, 246190, 246260, 253158, 253224, 253296, 253584, 257106, 260628, 267672, 274326, 274404, 274716, 295428, 295512, 295848, 316530, 316620, 316980, 320502, 334590, 369390, 369810] with properties: (84384, 9, 42193)
  Vector components: [178448, 182936, 196952, 197008, 213668, 223060, 246190, 246260, 253158, 253224, 253296, 253584, 257106, 260628, 267672, 274326, 274404, 274716, 295428, 295512, 295848, 316530, 316620, 316980, 320502, 334590, 369390, 369810]
  Squares of each component: [31843688704, 33465580096, 38790090304, 38812152064, 45654014224, 49755763600, 60609516100, 60643987600, 64088972964, 64122394176, 64158863616, 64304845056, 66103495236, 67926954384, 71648299584, 75254754276, 75297555216, 75468880656, 87277703184, 87327342144, 87526039104, 100191240900, 100248224400, 100476320400, 102721532004, 111950468100, 136448972100, 136759436100]
  Sum of squares: 2098877086292
  Magnitude before rounding: 1448750.1807737593
  The rounded magnitude of the vector is: 1448750

Vector: [194272, 208796, 209216, 222292, 223760, 223840, 242840, 261520, 268428, 268452, 268512, 268608, 268992, 271794, 285294, 285396, 285804, 291408, 313194, 313824, 333438, 335640, 335760, 336240, 364260, 392280] with properties: (89472, 3, 22369)
  Vector components: [194272, 208796, 209216, 222292, 223760, 223840, 242840, 261520, 268428, 268452, 268512, 268608, 268992, 271794, 285294, 285396, 285804, 291408, 313194, 313824, 333438, 335640, 335760, 336240, 364260, 392280]
  Squares of each component: [37741609984, 43595769616, 43771334656, 49413733264, 50068537600, 50104345600, 58971265600, 68392710400, 72053591184, 72066476304, 72098694144, 72150257664, 72356696064, 73871978436, 81392666436, 81450876816, 81683926416, 84918622464, 98090481636, 98485502976, 111180899844, 112654209600, 112734777600, 113057337600, 132685347600, 153883598400]
  Sum of squares: 2098875247904
  Magnitude before rounding: 1448749.5462998427
  The rounded magnitude of the vector is: 1448750

Magnitude 526490:
Vector: [183764, 236238, 236244, 236268, 275646] with properties: (78744, 3, 19687)
  Vector components: [183764, 236238, 236244, 236268, 275646]
  Squares of each component: [33769207696, 55808392644, 55811227536, 55822567824, 75980717316]
  Sum of squares: 277192113016
  Magnitude before rounding: 526490.3731465562
  The rounded magnitude of the vector is: 526490

Vector: [354126, 389598] with properties: (118040, 5, 59021)
  Vector components: [354126, 389598]
  Squares of each component: [125405223876, 151786601604]
  Sum of squares: 277191825480
  Magnitude before rounding: 526490.1000778647
  The rounded magnitude of the vector is: 526490

Magnitude 1075450:
Vector: [304336, 380420, 436134, 441618, 456504, 570630] with properties: (145376, 8, 72689)
  Vector components: [304336, 380420, 436134, 441618, 456504, 570630]
  Squares of each component: [92620400896, 144719376400, 190212865956, 195026457924, 208395902016, 325618596900]
  Sum of squares: 1156593600092
  Magnitude before rounding: 1075450.4173098824
  The rounded magnitude of the vector is: 1075450

Vector: [760434, 760482] with properties: (253476, 9, 126739)
  Vector components: [760434, 760482]
  Squares of each component: [578259868356, 578332872324]
  Sum of squares: 1156592740680
  Magnitude before rounding: 1075450.0177507089
  The rounded magnitude of the vector is: 1075450

Magnitude 453284:
Vector: [320442, 320598] with properties: (106812, 9, 53407)
  Vector components: [320442, 320598]
  Squares of each component: [102683075364, 102783077604]
  Sum of squares: 205466152968
  Magnitude before rounding: 453283.7444338811
  The rounded magnitude of the vector is: 453284

Vector: [320514, 320526] with properties: (106836, 6, 53419)
  Vector components: [320514, 320526]
  Squares of each component: [102729224196, 102736916676]
  Sum of squares: 205466140872
  Magnitude before rounding: 453283.7310912449
  The rounded magnitude of the vector is: 453284

Magnitude 2713383:
Vector: [323888, 365176, 373516, 391240, 402248, 404860, 424450, 456470, 457100, 469446, 469488, 469512, 477996, 481914, 485274, 485832, 502810, 508638, 516582, 517176, 547764, 560274, 586860, 586890, 587700, 603372, 607290, 646470, 685650] with properties: (156480, 6, 78241)
  Vector components: [323888, 365176, 373516, 391240, 402248, 404860, 424450, 456470, 457100, 469446, 469488, 469512, 477996, 481914, 485274, 485832, 502810, 508638, 516582, 517176, 547764, 560274, 586860, 586890, 587700, 603372, 607290, 646470, 685650]
  Squares of each component: [104903436544, 133353510976, 139514202256, 153068737600, 161803453504, 163911619600, 180157802500, 208364860900, 208940410000, 220379546916, 220418982144, 220441518144, 228480176016, 232241103396, 235490855076, 236032732224, 252817896100, 258712615044, 266856962724, 267471014976, 300045399696, 313906955076, 344404659600, 344439872100, 345391290000, 364057770384, 368801144100, 417923460900, 470115922500]
  Sum of squares: 7362447910996
  Magnitude before rounding: 2713383.1117252866
  The rounded magnitude of the vector is: 2713383

Vector: [1059716, 1362468, 1362492, 1589574] with properties: (454152, 3, 113539)
  Vector components: [1059716, 1362468, 1362492, 1589574]
  Squares of each component: [1122998000656, 1856319051024, 1856384450064, 2526745501476]
  Sum of squares: 7362447003220
  Magnitude before rounding: 2713382.9444477609
  The rounded magnitude of the vector is: 2713383

Magnitude 3403682:
Vector: [410168, 422296, 432824, 438724, 452420, 452440, 466100, 498550, 512710, 527870, 541030, 542886, 542898, 542904, 542928, 542952, 548628, 549414, 553302, 553638, 556488, 581622, 588198, 597234, 602862, 611358, 615252, 619146, 633444, 649236, 658086, 678630, 678660, 678690, 695610, 699150] with properties: (180960, 6, 90481)
  Vector components: [410168, 422296, 432824, 438724, 452420, 452440, 466100, 498550, 512710, 527870, 541030, 542886, 542898, 542904, 542928, 542952, 548628, 549414, 553302, 553638, 556488, 581622, 588198, 597234, 602862, 611358, 615252, 619146, 633444, 649236, 658086, 678630, 678660, 678690, 695610, 699150]
  Squares of each component: [168237788224, 178333911616, 187336614976, 192478748176, 204683856400, 204701953600, 217249210000, 248552102500, 262871544100, 278646736900, 292713460900, 294725208996, 294738238404, 294744753216, 294770813184, 294796874304, 300992682384, 301855743396, 306143103204, 306515035044, 309678894144, 338284150884, 345976887204, 356688450756, 363442591044, 373758604164, 378535023504, 383341769316, 401251301136, 421507383696, 433077183396, 460538676900, 460579395600, 460620116100, 483873272100, 488810722500]
  Sum of squares: 11585052801968
  Magnitude before rounding: 3403682.2416271470
  The rounded magnitude of the vector is: 3403682

Vector: [1899726, 1899738, 2089758] with properties: (633240, 9, 316621)
  Vector components: [1899726, 1899738, 2089758]
  Squares of each component: [3608958875076, 3609004468644, 4367088498564]
  Sum of squares: 11585051842284
  Magnitude before rounding: 3403682.1006498244
  The rounded magnitude of the vector is: 3403682

Magnitude 810684:
Vector: [573162, 573318] with properties: (191052, 9, 95527)
  Vector components: [573162, 573318]
  Squares of each component: [328514678244, 328693529124]
  Sum of squares: 657208207368
  Magnitude before rounding: 810683.7899995288
  The rounded magnitude of the vector is: 810684

Vector: [573234, 573246] with properties: (191076, 6, 95539)
  Vector components: [573234, 573246]
  Squares of each component: [328597218756, 328610976516]
  Sum of squares: 657208195272
  Magnitude before rounding: 810683.7825391600
  The rounded magnitude of the vector is: 810684

Magnitude 2437107:
Vector: [690220, 828246, 828264, 840498, 842874, 857994, 930666, 1035330] with properties: (276080, 5, 138041)
  Vector components: [690220, 828246, 828264, 840498, 842874, 857994, 930666, 1035330]
  Squares of each component: [476403648400, 685991436516, 686021253696, 706436888004, 710436579876, 736153704036, 866139203556, 1071908208900]
  Sum of squares: 5939490922984
  Magnitude before rounding: 2437107.0807381445
  The rounded magnitude of the vector is: 2437107

Vector: [1717116, 1729452] with properties: (572368, 4, 143093)
  Vector components: [1717116, 1729452]
  Squares of each component: [2948487357456, 2991004220304]
  Sum of squares: 5939491577760
  Magnitude before rounding: 2437107.2150728209
  The rounded magnitude of the vector is: 2437107

Magnitude 1066668:
Vector: [717492, 789294] with properties: (239160, 3, 59791)
  Vector components: [717492, 789294]
  Squares of each component: [514794770064, 622985018436]
  Sum of squares: 1137779788500
  Magnitude before rounding: 1066667.6091922920
  The rounded magnitude of the vector is: 1066668

Vector: [754242, 754254] with properties: (251412, 6, 125707)
  Vector components: [754242, 754254]
  Squares of each component: [568880994564, 568899096516]
  Sum of squares: 1137780091080
  Magnitude before rounding: 1066667.7510265321
  The rounded magnitude of the vector is: 1066668

Magnitude 1117910:
Vector: [790242, 790722] with properties: (263412, 9, 131707)
  Vector components: [790242, 790722]
  Squares of each component: [624482418564, 625241281284]
  Sum of squares: 1249723699848
  Magnitude before rounding: 1117910.4167365110
  The rounded magnitude of the vector is: 1117910

Vector: [790458, 790506] with properties: (263484, 9, 131743)
  Vector components: [790458, 790506]
  Squares of each component: [624823849764, 624899736036]
  Sum of squares: 1249723585800
  Magnitude before rounding: 1117910.3657270561
  The rounded magnitude of the vector is: 1117910

Magnitude 1310357:
Vector: [926322, 926802] with properties: (308772, 9, 154387)
  Vector components: [926322, 926802]
  Squares of each component: [858072447684, 858961947204]
  Sum of squares: 1717034394888
  Magnitude before rounding: 1310356.5907370406
  The rounded magnitude of the vector is: 1310357

Vector: [926538, 926586] with properties: (308844, 9, 154423)
  Vector components: [926538, 926586]
  Squares of each component: [858472665444, 858561615396]
  Sum of squares: 1717034280840
  Magnitude before rounding: 1310356.5472191146
  The rounded magnitude of the vector is: 1310357

Magnitude 2971478:
Vector: [974072, 1106900, 1328172, 1461108, 1660350] with properties: (442720, 1, 110681)
  Vector components: [974072, 1106900, 1328172, 1461108, 1660350]
  Squares of each component: [948816261184, 1225227610000, 1764040861584, 2134836587664, 2756762122500]
  Sum of squares: 8829683442932
  Magnitude before rounding: 2971478.3261757102
  The rounded magnitude of the vector is: 2971478

Vector: [2101146, 2101158] with properties: (700380, 9, 350191)
  Vector components: [2101146, 2101158]
  Squares of each component: [4414814513316, 4414864940964]
  Sum of squares: 8829679454280
  Magnitude before rounding: 2971477.6550194686
  The rounded magnitude of the vector is: 2971478

Magnitude 9339503:
Vector: [1078288, 1106456, 1191512, 1191568, 1291108, 1347860, 1489390, 1489460, 1531878, 1531884, 1531944, 1532016, 1532196, 1532304, 1553586, 1574868, 1617318, 1617432, 1659606, 1659684, 1659996, 1787268, 1787352, 1787562, 1787688, 1914930, 1915020, 1915380, 1936662, 2021790, 2234190, 2234610] with properties: (510624, 9, 255313)
  Vector components: [1078288, 1106456, 1191512, 1191568, 1291108, 1347860, 1489390, 1489460, 1531878, 1531884, 1531944, 1532016, 1532196, 1532304, 1553586, 1574868, 1617318, 1617432, 1659606, 1659684, 1659996, 1787268, 1787352, 1787562, 1787688, 1914930, 1915020, 1915380, 1936662, 2021790, 2234190, 2234610]
  Squares of each component: [1162705010944, 1224244879936, 1419700846144, 1419834298624, 1666959867664, 1816726579600, 2218282572100, 2218491091600, 2346650206884, 2346668589456, 2346852419136, 2347073024256, 2347624582416, 2347955548416, 2413629459396, 2480209217424, 2615717513124, 2616086274624, 2754292075236, 2754550979856, 2755586720016, 3194326903824, 3194627171904, 3195377903844, 3195828385344, 3666956904900, 3667301600400, 3668680544400, 3750659702244, 4087634804100, 4991604956100, 4993481852100]
  Sum of squares: 87226322486012
  Magnitude before rounding: 9339503.3318700623
  The rounded magnitude of the vector is: 9339503

Vector: [4741420, 5689686, 5689704] with properties: (1896560, 8, 948281)
  Vector components: [4741420, 5689686, 5689704]
  Squares of each component: [22481063616400, 32372526778596, 32372731607616]
  Sum of squares: 87226322002612
  Magnitude before rounding: 9339503.3059907425
  The rounded magnitude of the vector is: 9339503

Magnitude 1541292:
Vector: [1089618, 1090098] with properties: (363204, 9, 181603)
  Vector components: [1089618, 1090098]
  Squares of each component: [1187267385924, 1188313649604]
  Sum of squares: 2375581035528
  Magnitude before rounding: 1541292.0020320613
  The rounded magnitude of the vector is: 1541292

Vector: [1089834, 1089882] with properties: (363276, 9, 181639)
  Vector components: [1089834, 1089882]
  Squares of each component: [1187738147556, 1187842773924]
  Sum of squares: 2375580921480
  Magnitude before rounding: 1541291.9650345291
  The rounded magnitude of the vector is: 1541292

Magnitude 8271997:
Vector: [1294736, 1550276, 1618420, 1839462, 1839564, 1839888, 1865442, 1890996, 1941762, 1942104, 1993212, 2146158, 2146536, 2299860, 2325414, 2427630, 2683170] with properties: (613152, 9, 306577)
  Vector components: [1294736, 1550276, 1618420, 1839462, 1839564, 1839888, 1865442, 1890996, 1941762, 1942104, 1993212, 2146158, 2146536, 2299860, 2325414, 2427630, 2683170]
  Squares of each component: [1676341309696, 2403355676176, 2619283296400, 3383620449444, 3383995710096, 3385187852544, 3479873855364, 3575865872016, 3770439664644, 3771767946816, 3972894076944, 4605994160964, 4607616799296, 5289356019600, 5407550271396, 5893387416900, 7199401248900]
  Sum of squares: 68425931627196
  Magnitude before rounding: 8271996.8343318412
  The rounded magnitude of the vector is: 8271997

Vector: [5464712, 6209900] with properties: (2483920, 1, 620981)
  Vector components: [5464712, 6209900]
  Squares of each component: [29863077242944, 38562858010000]
  Sum of squares: 68425935252944
  Magnitude before rounding: 8271997.0534898043
  The rounded magnitude of the vector is: 8271997

Magnitude 7531283:
Vector: [1477528, 1591184, 1704740, 1988980, 2045676, 2045688, 2045808, 2216292, 2386776, 2557110, 2557260, 2983470] with properties: (681888, 3, 170473)
  Vector components: [1477528, 1591184, 1704740, 1988980, 2045676, 2045688, 2045808, 2216292, 2386776, 2557110, 2557260, 2983470]
  Squares of each component: [2183088990784, 2531866521856, 2906138467600, 3956041440400, 4184790296976, 4184839393344, 4185330372864, 4911950229264, 5696699674176, 6538811552100, 6539578707600, 8901093240900]
  Sum of squares: 56720228887864
  Magnitude before rounding: 7531283.3493279219
  The rounded magnitude of the vector is: 7531283

Vector: [3041860, 3650214, 3650232, 4562790] with properties: (1216736, 8, 608369)
  Vector components: [3041860, 3650214, 3650232, 4562790]
  Squares of each component: [9252912259600, 13324062245796, 13324193653824, 20819052584100]
  Sum of squares: 56720220743320
  Magnitude before rounding: 7531282.8086136831
  The rounded magnitude of the vector is: 7531283

Magnitude 6169920:
Vector: [1480952, 1682840, 1682900, 2019372, 2019408, 2091828, 2221428, 2524260, 2524350] with properties: (673120, 1, 168281)
  Vector components: [1480952, 1682840, 1682900, 2019372, 2019408, 2091828, 2221428, 2524260, 2524350]
  Squares of each component: [2193218826304, 2831950465600, 2832152410000, 4077863274384, 4078008670464, 4375744381584, 4934742359184, 6371888547600, 6372342922500]
  Sum of squares: 38067911857620
  Magnitude before rounding: 6169919.9231124548
  The rounded magnitude of the vector is: 6169920

Vector: [4355454, 4370118] with properties: (1451816, 8, 725909)
  Vector components: [4355454, 4370118]
  Squares of each component: [18969979546116, 19097931333924]
  Sum of squares: 38067910880040
  Magnitude before rounding: 6169919.8438910050
  The rounded magnitude of the vector is: 6169920

Magnitude 5507287:
Vector: [1553180, 1590140, 1863804, 1863816, 1908168, 1919262, 2329770, 2385210] with properties: (621264, 3, 155317)
  Vector components: [1553180, 1590140, 1863804, 1863816, 1908168, 1919262, 2329770, 2385210]
  Squares of each component: [2412368112400, 2528545219600, 3473765350416, 3473810081856, 3641105116224, 3683566624644, 5427828252900, 5689226744100]
  Sum of squares: 30330215502140
  Magnitude before rounding: 5507287.4904203070
  The rounded magnitude of the vector is: 5507287

Vector: [3894234, 3894246] with properties: (1298076, 6, 649039)
  Vector components: [3894234, 3894246]
  Squares of each component: [15165058446756, 15165151908516]
  Sum of squares: 30330210355272
  Magnitude before rounding: 5507287.0231423387
  The rounded magnitude of the vector is: 5507287

Magnitude 2473969:
Vector: [1749282, 1749438] with properties: (583092, 9, 291547)
  Vector components: [1749282, 1749438]
  Squares of each component: [3059987515524, 3060533315844]
  Sum of squares: 6120520831368
  Magnitude before rounding: 2473968.6399322040
  The rounded magnitude of the vector is: 2473969

Vector: [1749354, 1749366] with properties: (583116, 6, 291559)
  Vector components: [1749354, 1749366]
  Squares of each component: [3060239417316, 3060281401956]
  Sum of squares: 6120520819272
  Magnitude before rounding: 2473968.6374875489
  The rounded magnitude of the vector is: 2473969

Magnitude 5230455:
Vector: [2123502, 2123514, 2123658, 2134254, 2136978, 2169666] with properties: (707832, 9, 353917)
  Vector components: [2123502, 2123514, 2123658, 2134254, 2136978, 2169666]
  Squares of each component: [4509260744004, 4509311708196, 4509923300964, 4555040136516, 4566674972484, 4707450551556]
  Sum of squares: 27357661413720
  Magnitude before rounding: 5230455.1822685562
  The rounded magnitude of the vector is: 5230455

Vector: [3698466, 3698514] with properties: (1232820, 9, 616411)
  Vector components: [3698466, 3698514]
  Squares of each component: [13678650753156, 13679005808196]
  Sum of squares: 27357656561352
  Magnitude before rounding: 5230454.7184113925
  The rounded magnitude of the vector is: 5230455

Magnitude 3135765:
Vector: [2167446, 2266098] with properties: (722480, 5, 361241)
  Vector components: [2167446, 2266098]
  Squares of each component: [4697822162916, 5135200145604]
  Sum of squares: 9833022308520
  Magnitude before rounding: 3135765.0276320130
  The rounded magnitude of the vector is: 3135765

Vector: [2217318, 2217324] with properties: (739104, 6, 369553)
  Vector components: [2217318, 2217324]
  Squares of each component: [4916499113124, 4916525720976]
  Sum of squares: 9833024834100
  Magnitude before rounding: 3135765.4303375436
  The rounded magnitude of the vector is: 3135765

Magnitude 3092546:
Vector: [2186682, 2186838] with properties: (728892, 9, 364447)
  Vector components: [2186682, 2186838]
  Squares of each component: [4781578169124, 4782260438244]
  Sum of squares: 9563838607368
  Magnitude before rounding: 3092545.6516223005
  The rounded magnitude of the vector is: 3092546

Vector: [2186754, 2186766] with properties: (728916, 6, 364459)
  Vector components: [2186754, 2186766]
  Squares of each component: [4781893056516, 4781945538756]
  Sum of squares: 9563838595272
  Magnitude before rounding: 3092545.6496666302
  The rounded magnitude of the vector is: 3092546

Magnitude 8731673:
Vector: [2225500, 2237500, 2448050, 2461250, 2670006, 2697306, 2937066, 2965314, 3338250, 3356250] with properties: (890000, 8, 445001)
  Vector components: [2225500, 2237500, 2448050, 2461250, 2670006, 2697306, 2937066, 2965314, 3338250, 3356250]
  Squares of each component: [4952850250000, 5006406250000, 5992948802500, 6057751562500, 7128932040036, 7275459657636, 8626356688356, 8793087118596, 11143913062500, 11264414062500]
  Sum of squares: 76242119494624
  Magnitude before rounding: 8731673.3502017818
  The rounded magnitude of the vector is: 8731673

Vector: [6174222, 6174228] with properties: (2058072, 6, 1029037)
  Vector components: [6174222, 6174228]
  Squares of each component: [38121017305284, 38121091395984]
  Sum of squares: 76242108701268
  Magnitude before rounding: 8731672.7321440540
  The rounded magnitude of the vector is: 8731673

Magnitude 8805829:
Vector: [2379356, 2569640, 3059148, 3059172, 3075396, 3083568, 3569034, 3854460] with properties: (1019712, 3, 254929)
  Vector components: [2379356, 2569640, 3059148, 3059172, 3075396, 3083568, 3569034, 3854460]
  Squares of each component: [5661334974736, 6603049729600, 9358386485904, 9358533325584, 9458060556816, 9508391610624, 12738003693156, 14856861891600]
  Sum of squares: 77542622268020
  Magnitude before rounding: 8805828.8802372254
  The rounded magnitude of the vector is: 8805829

Vector: [6108652, 6342476] with properties: (2630160, 9, 1315081)
  Vector components: [6108652, 6342476]
  Squares of each component: [37315629257104, 40227001810576]
  Sum of squares: 77542631067680
  Magnitude before rounding: 8805829.3798869401
  The rounded magnitude of the vector is: 8805829

Magnitude 7059989:
Vector: [2464084, 3168078, 3168084, 3168108, 3696126] with properties: (1056024, 9, 528013)
  Vector components: [2464084, 3168078, 3168084, 3168108, 3696126]
  Squares of each component: [6071709959056, 10036718214084, 10036756231056, 10036908299664, 13661347407876]
  Sum of squares: 49843440111736
  Magnitude before rounding: 7059988.6764594745
  The rounded magnitude of the vector is: 7059989

Vector: [3922806, 3979266, 4315146] with properties: (1307600, 8, 653801)
  Vector components: [3922806, 3979266, 4315146]
  Squares of each component: [15388406913636, 15834557898756, 18620485001316]
  Sum of squares: 49843449813708
  Magnitude before rounding: 7059989.3635690417
  The rounded magnitude of the vector is: 7059989

Magnitude 3825674:
Vector: [2705082, 2705238] with properties: (901692, 9, 450847)
  Vector components: [2705082, 2705238]
  Squares of each component: [7317468626724, 7318312636644]
  Sum of squares: 14635781263368
  Magnitude before rounding: 3825673.9619795098
  The rounded magnitude of the vector is: 3825674

Vector: [2705154, 2705166] with properties: (901716, 6, 450859)
  Vector components: [2705154, 2705166]
  Squares of each component: [7317858163716, 7317923087556]
  Sum of squares: 14635781251272
  Magnitude before rounding: 3825673.9603986121
  The rounded magnitude of the vector is: 3825674

Magnitude 4439669:
Vector: [3139242, 3139398] with properties: (1046412, 9, 523207)
  Vector components: [3139242, 3139398]
  Squares of each component: [9854840334564, 9855819802404]
  Sum of squares: 19710660136968
  Magnitude before rounding: 4439668.9219994769
  The rounded magnitude of the vector is: 4439669

Vector: [3139314, 3139326] with properties: (1046436, 6, 523219)
  Vector components: [3139314, 3139326]
  Squares of each component: [9855292390596, 9855367734276]
  Sum of squares: 19710660124872
  Magnitude before rounding: 4439668.9206372136
  The rounded magnitude of the vector is: 4439669

Magnitude 5195707:
Vector: [3673842, 3673998] with properties: (1224612, 9, 612307)
  Vector components: [3673842, 3673998]
  Squares of each component: [13497115040964, 13498261304004]
  Sum of squares: 26995376344968
  Magnitude before rounding: 5195707.4922447279
  The rounded magnitude of the vector is: 5195707

Vector: [3673914, 3673926] with properties: (1224636, 6, 612319)
  Vector components: [3673914, 3673926]
  Squares of each component: [13497644079396, 13497732253476]
  Sum of squares: 26995376332872
  Magnitude before rounding: 5195707.4910806902
  The rounded magnitude of the vector is: 5195707

Magnitude 5317132:
Vector: [3759702, 3759858] with properties: (1253232, 9, 626617)
  Vector components: [3759702, 3759858]
  Squares of each component: [14135359128804, 14136532180164]
  Sum of squares: 28271891308968
  Magnitude before rounding: 5317131.8686833410
  The rounded magnitude of the vector is: 5317132

Vector: [3759774, 3759786] with properties: (1253256, 6, 626629)
  Vector components: [3759774, 3759786]
  Squares of each component: [14135900531076, 14135990765796]
  Sum of squares: 28271891296872
  Magnitude before rounding: 5317131.8675458860
  The rounded magnitude of the vector is: 5317132

Magnitude 8140592:
Vector: [3869214, 3900678, 3962106, 4514958] with properties: (1289736, 9, 644869)
  Vector components: [3869214, 3900678, 3962106, 4514958]
  Squares of each component: [14970816977796, 15215288859684, 15698283955236, 20384845741764]
  Sum of squares: 66269235534480
  Magnitude before rounding: 8140591.8417815296
  The rounded magnitude of the vector is: 8140592

Vector: [5700876, 5811132] with properties: (1900288, 1, 475073)
  Vector components: [5700876, 5811132]
  Squares of each component: [32499987167376, 33769255121424]
  Sum of squares: 66269242288800
  Magnitude before rounding: 8140592.2566358773
  The rounded magnitude of the vector is: 8140592

Magnitude 6801102:
Vector: [3926562, 3926574, 3926718] with properties: (1308852, 9, 654427)
  Vector components: [3926562, 3926574, 3926718]
  Squares of each component: [15417889139844, 15417983377476, 15419114251524]
  Sum of squares: 46254986768844
  Magnitude before rounding: 6801101.8790225452
  The rounded magnitude of the vector is: 6801102

Vector: [4809102, 4809108] with properties: (1603032, 6, 801517)
  Vector components: [4809102, 4809108]
  Squares of each component: [23127462046404, 23127519755664]
  Sum of squares: 46254981802068
  Magnitude before rounding: 6801101.5138775865
  The rounded magnitude of the vector is: 6801102

Magnitude 5708897:
Vector: [4036722, 4036878] with properties: (1345572, 9, 672787)
  Vector components: [4036722, 4036878]
  Squares of each component: [16295124505284, 16296383986884]
  Sum of squares: 32591508492168
  Magnitude before rounding: 5708897.3096534153
  The rounded magnitude of the vector is: 5708897

Vector: [4036794, 4036806] with properties: (1345596, 6, 672799)
  Vector components: [4036794, 4036806]
  Squares of each component: [16295705798436, 16295802681636]
  Sum of squares: 32591508480072
  Magnitude before rounding: 5708897.3085940164
  The rounded magnitude of the vector is: 5708897

Magnitude 6066297:
Vector: [4289442, 4289598] with properties: (1429812, 9, 714907)
  Vector components: [4289442, 4289598]
  Squares of each component: [18399312671364, 18400651001604]
  Sum of squares: 36799963672968
  Magnitude before rounding: 6066297.3610735573
  The rounded magnitude of the vector is: 6066297

Vector: [4289514, 4289526] with properties: (1429836, 6, 714919)
  Vector components: [4289514, 4289526]
  Squares of each component: [18399930356196, 18400033304676]
  Sum of squares: 36799963660872
  Magnitude before rounding: 6066297.3600765727
  The rounded magnitude of the vector is: 6066297

Magnitude 6356597:
Vector: [4393758, 4593606] with properties: (1464584, 5, 732293)
  Vector components: [4393758, 4593606]
  Squares of each component: [19305109362564, 21101216083236]
  Sum of squares: 40406325445800
  Magnitude before rounding: 6356597.0019972166
  The rounded magnitude of the vector is: 6356597

Vector: [4483932, 4505628] with properties: (1494640, 1, 373661)
  Vector components: [4483932, 4505628]
  Squares of each component: [20105646180624, 20300683674384]
  Sum of squares: 40406329855008
  Magnitude before rounding: 6356597.3488186272
  The rounded magnitude of the vector is: 6356597

Magnitude 6726342:
Vector: [4756002, 4756482] with properties: (1585332, 9, 792667)
  Vector components: [4756002, 4756482]
  Squares of each component: [22619555024004, 22624121016324]
  Sum of squares: 45243676040328
  Magnitude before rounding: 6726341.9508918812
  The rounded magnitude of the vector is: 6726342

Vector: [4756218, 4756266] with properties: (1585404, 9, 792703)
  Vector components: [4756218, 4756266]
  Squares of each component: [22621609663524, 22622066262756]
  Sum of squares: 45243675926280
  Magnitude before rounding: 6726341.9424141683
  The rounded magnitude of the vector is: 6726342

Magnitude 7065185:
Vector: [4995762, 4995918] with properties: (1665252, 9, 832627)
  Vector components: [4995762, 4995918]
  Squares of each component: [24957637960644, 24959196662724]
  Sum of squares: 49916834623368
  Magnitude before rounding: 7065184.6843071273
  The rounded magnitude of the vector is: 7065185

Vector: [4995834, 4995846] with properties: (1665276, 6, 832639)
  Vector components: [4995834, 4995846]
  Squares of each component: [24958357355556, 24958477255716]
  Sum of squares: 49916834611272
  Magnitude before rounding: 7065184.6834510984
  The rounded magnitude of the vector is: 7065185

Magnitude 9445102:
Vector: [5213046, 5287938, 5837106] with properties: (1737680, 5, 868841)
  Vector components: [5213046, 5287938, 5837106]
  Squares of each component: [27175848598116, 27962288291844, 34071806455236]
  Sum of squares: 89209943345196
  Magnitude before rounding: 9445101.5529318694
  The rounded magnitude of the vector is: 9445102

Vector: [6678618, 6678774] with properties: (2226204, 9, 1113103)
  Vector components: [6678618, 6678774]
  Squares of each component: [44603938389924, 44606022143076]
  Sum of squares: 89209960533000
  Magnitude before rounding: 9445102.4628110845
  The rounded magnitude of the vector is: 9445102

Magnitude 7763356:
Vector: [5222172, 5744442] with properties: (1740720, 3, 435181)
  Vector components: [5222172, 5744442]
  Squares of each component: [27271080397584, 32998613891364]
  Sum of squares: 60269694288948
  Magnitude before rounding: 7763355.8651492978
  The rounded magnitude of the vector is: 7763356

Vector: [5366076, 5610252] with properties: (1788688, 1, 447173)
  Vector components: [5366076, 5610252]
  Squares of each component: [28794771637776, 31474927503504]
  Sum of squares: 60269699141280
  Magnitude before rounding: 7763356.1776644001
  The rounded magnitude of the vector is: 7763356

Magnitude 7838283:
Vector: [5502846, 5581878] with properties: (1834280, 8, 917141)
  Vector components: [5502846, 5581878]
  Squares of each component: [30281314099716, 31157362006884]
  Sum of squares: 61438676106600
  Magnitude before rounding: 7838282.7268860368
  The rounded magnitude of the vector is: 7838283

Vector: [5523366, 5561574] with properties: (1841120, 8, 920561)
  Vector components: [5523366, 5561574]
  Squares of each component: [30507571969956, 30931105357476]
  Sum of squares: 61438677327432
  Magnitude before rounding: 7838282.8047622778
  The rounded magnitude of the vector is: 7838283

Magnitude 11092915:
Vector: [5631580, 6757878, 6757896] with properties: (2252624, 5, 1126313)
  Vector components: [5631580, 6757878, 6757896]
  Squares of each component: [31714693296400, 45668915062884, 45669158346816]
  Sum of squares: 123052766706100
  Magnitude before rounding: 11092915.1581583824
  The rounded magnitude of the vector is: 11092915

Vector: [6301956, 6318966, 6588534] with properties: (2100648, 3, 525163)
  Vector components: [6301956, 6318966, 6588534]
  Squares of each component: [39714649425936, 39929331309156, 43408780269156]
  Sum of squares: 123052761004248
  Magnitude before rounding: 11092914.9011541605
  The rounded magnitude of the vector is: 11092915

Magnitude 8375652:
Vector: [5922402, 5922558] with properties: (1974132, 9, 987067)
  Vector components: [5922402, 5922558]
  Squares of each component: [35074845449604, 35076693263364]
  Sum of squares: 70151538712968
  Magnitude before rounding: 8375651.5396097992
  The rounded magnitude of the vector is: 8375652

Vector: [5922474, 5922486] with properties: (1974156, 6, 987079)
  Vector components: [5922474, 5922486]
  Squares of each component: [35075698280676, 35075840420196]
  Sum of squares: 70151538700872
  Magnitude before rounding: 8375651.5388877066
  The rounded magnitude of the vector is: 8375652

Magnitude 8623311:
Vector: [6097362, 6097842] with properties: (2032452, 9, 1016227)
  Vector components: [6097362, 6097842]
  Squares of each component: [37177823359044, 37183677056964]
  Sum of squares: 74361500416008
  Magnitude before rounding: 8623311.4530328773
  The rounded magnitude of the vector is: 8623311

Vector: [6097578, 6097626] with properties: (2032524, 9, 1016263)
  Vector components: [6097578, 6097626]
  Squares of each component: [37180457466084, 37181042835876]
  Sum of squares: 74361500301960
  Magnitude before rounding: 8623311.4464201052
  The rounded magnitude of the vector is: 8623311

Magnitude 8865931:
Vector: [6269082, 6269238] with properties: (2089692, 9, 1044847)
  Vector components: [6269082, 6269238]
  Squares of each component: [39301389122724, 39303345100644]
  Sum of squares: 78604734223368
  Magnitude before rounding: 8865931.0973731354
  The rounded magnitude of the vector is: 8865931

Vector: [6269154, 6269166] with properties: (2089716, 6, 1044859)
  Vector components: [6269154, 6269166]
  Squares of each component: [39302291875716, 39302442335556]
  Sum of squares: 78604734211272
  Magnitude before rounding: 8865931.0966909733
  The rounded magnitude of the vector is: 8865931

Total number of magnitude sets: 46
```
