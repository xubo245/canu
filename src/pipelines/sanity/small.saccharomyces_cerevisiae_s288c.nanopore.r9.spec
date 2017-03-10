gridOptions=-q big.q

genomeSize=12.1m
stopOnReadQuality=false

#
#  -- In gatekeeper store 'correction/test.gkpStore':
#  --   Found 321777 reads.
#  --   Found 2222909819 bases (463.1 times coverage).
#  --
#  --   Read length histogram (one '*' equals 584.81 reads):
#  --        0    999      0 
#  --     1000   1999  40937 **********************************************************************
#  --     2000   2999  32782 ********************************************************
#  --     3000   3999  31752 ******************************************************
#  --     4000   4999  33865 *********************************************************
#  --     5000   5999  35473 ************************************************************
#  --     6000   6999  38523 *****************************************************************
#  --     7000   7999  26724 *********************************************
#  --     8000   8999  20353 **********************************
#  --     9000   9999  14632 *************************
#  --    10000  10999   9716 ****************
#  --    11000  11999   6740 ***********
#  --    12000  12999   5075 ********
#  --    13000  13999   3503 *****
#  --    14000  14999   2690 ****
#  --    15000  15999   2121 ***
#  --    16000  16999   1816 ***
#  --    17000  17999   1461 **
#  --    18000  18999   1352 **
#  --    19000  19999   1237 **
#  --    20000  20999    999 *
#  --    21000  21999    864 *
#  --    22000  22999    764 *
#  --    23000  23999    714 *
#  --    24000  24999    587 *
#  --    25000  25999    528 
#  --    26000  26999    510 
#  --    27000  27999    471 
#  --    28000  28999    383 
#  --    29000  29999    361 
#  --    30000  30999    303 
#  --    31000  31999    335 
#  --    32000  32999    288 
#  --    33000  33999    244 
#  --    34000  34999    214 
#  --    35000  35999    196 
#  --    36000  36999    193 
#  --    37000  37999    190 
#  --    38000  38999    186 
#  --    39000  39999    172 
#  --    40000  40999    143 
#  --    41000  41999    127 
#  --    42000  42999    122 
#  --    43000  43999    109 
#  --    44000  44999    103 
#  --    45000  45999     83 
#  --    46000  46999     86 
#  --    47000  47999     86 
#  --    48000  48999     80 
#  --    49000  49999     79 
#  --    50000  50999     71 
#  --    51000  51999     61 
#  --    52000  52999     48 
#  --    53000  53999     66 
#  --    54000  54999     64 
#  --    55000  55999     42 
#  --    56000  56999     47 
#  --    57000  57999     38 
#  --    58000  58999     47 
#  --    59000  59999     33 
#  --    60000  60999     45 
#  --    61000  61999     35 
#  --    62000  62999     41 
#  --    63000  63999     43 
#  --    64000  64999     28 
#  --    65000  65999     38 
#  --    66000  66999     29 
#  --    67000  67999     25 
#  --    68000  68999     23 
#  --    69000  69999     26 
#  --    70000  70999     23 
#  --    71000  71999     22 
#  --    72000  72999     24 
#  --    73000  73999     20 
#  --    74000  74999     17 
#  --    75000  75999     20 
#  --    76000  76999     16 
#  --    77000  77999     10 
#  --    78000  78999     14 
#  --    79000  79999      9 
#  --    80000  80999     16 
#  --    81000  81999     13 
#  --    82000  82999     12 
#  --    83000  83999     12 
#  --    84000  84999      8 
#  --    85000  85999      8 
#  --    86000  86999     15 
#  --    87000  87999     11 
#  --    88000  88999     11 
#  --    89000  89999      8 
#  --    90000  90999      9 
#  --
#  --  Max: 414k
#

-nanopore-raw /data/regression/reads/saccharomyces_cerevisiae_s288c.nanopore.r9.fastq.xz

onSuccess=/work/canu/src/pipelines/sanity/success.saccharomyces_cerevisiae_s288c.sh