# thirteenth

"Flavored Datetime Converter"

## Initialize

(Overwrote `__repr__`)

``` python console
>>> from thirteenth import Thirteenth

>>> Thirteenth()                        # Now, via `time.time_ns`.
<3Y,0M,1W,4D; 22h,41m,12s; 127ms,132us,925ns>

>>> Thirteenth('2021-04-26 14:23:33')   # From datetime (via `time.strptime`), cannot specify nanoseconds.
<3Y,0M,1W,4D; 22h,41m,11s; 951ms,192us,442ns>

>>> Thirteenth('20210426', '%Y%m%d')    # Datetime with customized format.
<3Y,0M,1W,4D; 8h,47m,22s; 258ms,781us,263ns>

>>> Thirteenth('2016-09-01 00:00:00')   # Gave datetime should not before this, otherwise `ValueError` will be raised.
<0Y,0M,0W,0D; 0h,0m,0s; 80ms,276us,903ns>
```

## CLI

(Overwrote `__str__`)

``` shell
$ python -m thirteenth
03-0-1-4 23:33:20 25D17807
```

## Attributes

### General

``` python console
>>> a = Thirteenth()
>>> a
<3Y,0M,1W,4D; 23h,10m,51s; 310ms,68us,237ns>
>>> a.year
3
>>> a.month
0
>>> a.week
1
>>> a.day
4
>>> a.hour
23
>>> a.minute
10
>>> a.second
51
>>> a.millisecond
310
>>> a.microsecond
68
>>> a.nanosecond
237
```

### Total

``` python console
>>> a.total_month
39
>>> a.total_day
1572
>>> a.total_second
146321544
```

### For

"For the progress of span A, how many spans B is equivalent"

``` python console
>>> a.for_year_day
12
>>> a.for_year_minute
19713
```