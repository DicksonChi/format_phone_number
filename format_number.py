import csv
import re


def st_str(s):
    """Strip out all hyphen and space from the string."""
    s = re.sub('[- ]', '', s)
    return s


def get_amount_hyphen(s):
    """Get the amount of hyphen needed."""
    if len(s) % 3 > 0:
        return (len(s) - (len(s) % 3))/3
    else:
        return (len(s)/3) - 1


def add_hyphen_to_string(s):
    """Add the hyphen to the stripped out string to form a formatted phone number"""
    s = st_str(s)
    amt_hyphen = get_amount_hyphen(s)

    j_start = 0
    j_end = 3
    new_number = ''
    for i in range(0, int(amt_hyphen)):
        if i+1 == amt_hyphen and len(s[j_end:]) == 1:
            new_number = '{}{}-'.format(new_number, s[j_start:j_end-1])
            j_start += 2
        else:
            new_number = '{}{}-'.format(new_number, s[j_start:j_end])
            j_start += 3
        j_end += 3
    return '{}{}'.format(new_number, s[j_start:])


def format_rows(path_to_csv):
    """Format phone numbers of all data from csv and return array"""
    # run through the rows
    result = []
    line = -1
    with open(path_to_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if line > -1:
                result.append(add_hyphen_to_string(row[0]))
            line += 1
    print('{} phone numbers have been formatted.'.format(line))
    print(result)


if __name__ == '__main__':
    # format numbers
    format_rows('phone_numbers.csv')
