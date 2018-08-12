# Upchieve school parser

A parser that filters highschools from a schools .csv data set.


## How to use it

1. Download the raw data from the [National Center for Education Statistics website](https://nces.ed.gov/ccd/pubschuniv.asp) and **make sure that it doesn't contain any empty lines**
1. Rename `config.example` to `config.py`
1. Run the program
```
python -m parser <path/to/raw_data.csv>
```

## Running tests

1. Change the constants `FILE_PATH_IN` and `FILE_PATH_OUT` in `config.py`
1. Run the test suite
```
python -m test
```


## Possible future improvements

- [ ] Format school names (limit formatting to that specific field to avoid false positives)
    - [ ] Convert to *Proper Case*, while being careful with Irish surnames
    - [ ] Change `Sch` to `School`
    - [ ] Change `Acad` to `Academy`
    - [ ] Change `Lrng` to `Learning`
    - [ ] Change `Jhs/JHS` to `Junior High School`
    - [ ] Change `Shs/SHS` to `Senior High School`
    - [ ] Change `Hs/HS` to `High School`