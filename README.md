# format_phone_number

## Installation
```
 git clone git@github.com:DicksonChi/format_phone_number.git
 cd format_phone_number
 python format_number.py
```

You can add your numbers to the `phone_numbers.csv` file

#### How it works.
This goes through a CSV file with phone numbers that are in wrong format eg "0 - 22 1985--324" and the is expected to 
format them into a string with group of 3's separated with a hyphen, with a condition that the last group must not be 1.

eg. "0 - 22 1985--324" will give "022-198-53-24" 

"333 -3 -3-333" will give "333-333-33"
